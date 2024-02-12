# Andrei Merkulov, 251145994
# 2023 / 10 / 02

import socket
import os

def main():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9200))
    server_socket.listen(3)

    while True:
        # Accept incoming connections
        client_socket, address = server_socket.accept()

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')

        # Parse the HTTP GET request
        request_method = data.split(' ')[0]
        requested_file = data.split(' ')[1]

        # Search for the requested file in the server's file system
        if requested_file == '/':
            requested_file = '/hello.html'

        file_path = os.getcwd() + '/files' + requested_file

        if os.path.isfile(file_path):
            # If the file is found, create an HTTP response message including the header and the requested file
            with open(file_path, 'rb') as file:
                file_data = file.read()

            response_header = 'HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n'.format(len(file_data)).encode('utf-8')
            response_data = response_header + file_data

            client_socket.send(response_data)
        else:
            # If the file is not found, send a 404 HTTP message to the client
            response_header = 'HTTP/1.1 404 Not Found\n\n'.encode('utf-8')
            response_data = response_header + b'The requested file was not found on this server.'

            client_socket.send(response_data)

        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    main()
