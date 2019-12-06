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
                    connection.sendall('Send me the word int and i will send you a random integar between 0 and 1 000 000 \n'.encode()                                       
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


def handle_random(ip, port):
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
            if meessage == "get":
                connection.sendall(str(randint(0, 1000000)).encode())
            else:
                connection.sendall("Incorrect message".encode())
        except:
            print("Error handling request")
        finally:
            connection.close()



