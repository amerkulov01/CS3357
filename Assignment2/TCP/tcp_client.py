import socket
import select
import threading
import argparse
import sys

HOST = '127.0.0.1'
PORT = 9301
BUFFER_SIZE = 1024
# this function is called in a separate thread to receive messages from the server
def receive_messages(client_socket, name):
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE)   # receive message from server
            if message:
                message_str = message.decode().strip()  # convert message to string
                if message_str.startswith(name + ':'):  # if message is from another client
                    print(message_str)
                else:
                    print(message_str)
            else:
                raise Exception('Server disconnected')
        except:
            client_socket.close()
            print('Disconnected from server')
            return

def send_message(client_socket, name, message): # this function is called in the main thread to send messages to the server
    sys.stdout.write("\033[F") # Move cursor up one line
    sys.stdout.write("\033[K") # Clear line
    print(f'{name}: {message}') # Print message locally
    client_socket.send(f'{name}: {message}\n'.encode()) # Send message to server

if __name__ == '__main__':  # this is the main thread
    parser = argparse.ArgumentParser(description='TCP Chatroom Client')
    parser.add_argument('name', help='Your username')
    args = parser.parse_args()  # parse command line arguments

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create TCP socket
    client_socket.connect((HOST, PORT)) # connect to server

    threading.Thread(target=receive_messages, args=(client_socket, args.name)).start()  

    while True:
        message = input()
        if message == 'exit':
            client_socket.close()
            break
        send_message(client_socket, args.name, message)
