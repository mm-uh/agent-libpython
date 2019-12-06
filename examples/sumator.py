from __future__ import print_function

import ctypes
import socket
import sys
import threading

import lib_agent
from lib_agent.rest import ApiException


def handle_documentation(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (ip, port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                    connection.sendall('You must pass 2 numbers separated by spaces. \n'
                                       'This agent just sum both numbers and return that sum in string\n'.encode())
                else:
                    print('no data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()


def handle_is_alive(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (ip, port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        while True:
            print('connection from', client_address)
            data = connection.recv(16)
            if not data:
                break
            message = data.decode()

            if 'IsAlive?' in message:
                connection.send('Yes'.encode())
        # Clean up the connection
        connection.close()


def handle_sum(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (ip, port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            data = connection.recv(16)
            message = data.decode()

            nums = message.split(' ')
            if len(nums) != 2:
                connection.sendall("-1".encode())
            else:
                try:
                    add = int(nums[0]) + int(nums[1])
                    connection.sendall(str(add).encode())
                except Exception as e:
                    print(f'Error sending sum response {e}')
            # Receive the data in small chunks and retransmit it
        finally:
            # Clean up the connection
            connection.close()


def terminate_thread(thread):
    """Terminates a python thread from another thread.

    :param thread: a threading.Thread instance
    """
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def main():
    name = 'Adder'
    function = 'Add'
    host = sys.argv[1]
    port = int(sys.argv[2])
    myIp = sys.argv[3]
    myPort = int(sys.argv[4])
    
    wrapper = lib_agent.PlatformWrapper(host, port)
    # wrapper = lib_agent.PlatformWrapper(host, port)

    test_case = [
        lib_agent.TestCase('1 2', '3'),
        lib_agent.TestCase('2 3', '5'),
    ]
    endpoint_service = [
        lib_agent.Addr(f'{myIp}', 38080),
        lib_agent.Addr(f'{myIp}', 38085),
    ]
    
    is_alive_service = dict()
    is_alive_service[f'{myIp}:38080'] = lib_agent.Addr(f'{myIp}', 38081)
    is_alive_service[f'{myIp}:38085'] = lib_agent.Addr(f'{myIp}', 38086)

    documentation = dict()
    documentation[f'{myIp}:38080'] = lib_agent.Addr(f'{myIp}', 38082)
    documentation[f'{myIp}:38085'] = lib_agent.Addr(f'{myIp}', 38086)

    # Agent | Agent to register
    agent = lib_agent.Agent(name=name, function=function, endpoint_service=endpoint_service,
                            documentation=documentation, is_alive_service=is_alive_service, test_cases=test_case)

    sum_server = threading.Thread(target=handle_sum, args=(f'{myIp}', myPort))
    sum_server.start()

    is_alive_server = threading.Thread(target=handle_is_alive, args=(f'{myIp}', myPort+1))
    is_alive_server.start()

    doc_server = threading.Thread(target=handle_documentation, args=(f'{myIp}', myPort+2))
    doc_server.start()

    # Get Know peers
    try:
       
        wrapper.get_peers()
        print(wrapper.know_peers)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_peers: %s\n" % e)

    # Register Agent
    try:
        print("Registering")
        wrapper.register_agent(agent)
        print(wrapper.know_peers)
        print("Registered")
    except ApiException as e:
        print("Exception when calling DefaultApi->register_agent: %s\n" % e)
    ag = None
    # Get Agent
    try:
        ag = wrapper.get_agent(name)
        print(ag)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_agent: %s\n" % e)

    # Get registered functions
    try:
        functions_names = wrapper.get_agent_by_function(function)
        print(functions_names)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_agent_by_function: %s\n" % e)

    #Run agent
    # try:
        # response = wrapper.run_agent(agent.name, '1 2')
        # print(response)
    # except ApiException as e:
        # print("Exception when calling DefaultApi->get_agent_by_function: %s\n" % e)
# 
    #Run agent
    # try:
        # response = wrapper.run_agent(agent.name, '1 2')
        # print(response)
    # except ApiException as e:
        # print("Exception when calling DefaultApi->get_agent_by_function: %s\n" % e)

    sum_server.join()
    is_alive_server.join()
    doc_server.join()


if __name__ == '__main__':
    main()
