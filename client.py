# Andrei Merkulov, 251145994
# 2023 / 10 / 02

import socket
import sys

def main():
    # Set up the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9200))

    # Send an HTTP GET request to the server
    request = 'GET /{} HTTP/1.1\nHost: localhost:9200\n\n'.format(sys.argv[2]).encode('utf-8')
    client_socket.send(request)

    # Receive data from the server
    response = client_socket.recv(1024)

    # Parse the HTTP response message
    response_data = response.split(b'\n\n')[1]

    # If a file is returned, save that file
    with open(sys.argv[2], 'wb') as file:
        file.write(response_data)

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    main()