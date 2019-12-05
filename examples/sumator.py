from __future__ import print_function

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
                    connection.sendall(bytes('You must pass 2 numbers separated by spaces. \n'
                                             'This agent just sum both numbers and return that sum in string\n'))
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
                print('number of send bytes')
                print(connection.send('Yes'.encode()))
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
                connection.sendall(bytes("-1\n"))
            else:
                try:
                    connection.sendall(bytes(f"{float(nums[0]) + float(nums[1])}\n"))
                except:
                    pass
            # Receive the data in small chunks and retransmit it
        finally:
            # Clean up the connection
            connection.close()


def main():
    name = 'Adder'
    function = 'Add'
    host = sys.argv[1]
    port = int(sys.argv[2])
    wrapper = lib_agent.AgentWrapper(host, port)

    test_case = [
        lib_agent.TestCase('1 2', '3'),
        lib_agent.TestCase('2 3', '5'),
    ]
    endpoint_service = [
        lib_agent.Addr('localhost', 38080),
    ]

    is_alive_service = dict()
    is_alive_service['localhost:38080'] = lib_agent.Addr('localhost', 38081)

    documentation = dict()
    documentation['localhost:38080'] = lib_agent.Addr('localhost', 38082)

    # Agent | Agent to register
    agent = lib_agent.Agent(name=name, function=function, endpoint_service=endpoint_service,
                            documentation=documentation, is_alive_service=is_alive_service, test_cases=test_case)

    sum_server = threading.Thread(target=handle_sum, args=('localhost', 38080))
    sum_server.start()

    is_alive_server = threading.Thread(target=handle_is_alive, args=('localhost', 38081))
    is_alive_server.start()

    doc_server = threading.Thread(target=handle_documentation, args=('localhost', 38082))
    doc_server.start()

    # Get Know peers
    try:
        wrapper.get_peers()
        print(wrapper.know_peers)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_peers: %s\n" % e)

    # Register Agent
    try:
        wrapper.register_agent(agent)
        print(wrapper.know_peers)
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

    # Run agent
    try:
        response = wrapper.run_agent(agent.name, '1 2')
        print(response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_agent_by_function: %s\n" % e)

    sum_server.join()
    is_alive_server.join()
    doc_server.join()


if __name__ == '__main__':
    main()
