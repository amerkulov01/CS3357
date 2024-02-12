# Assignment: UDP Simple Chat Room - UDP Client Code Implementation

# Libraries and Imports
import socket
import threading
import sys

# Global Variables
RECV_BUFFER = 4096

# Function Definitions
def receive_messages(client_socket):
    while True:
        data, _ = client_socket.recvfrom(RECV_BUFFER)
        message = data.decode()
        print(message)

def run(server_addr, server_port, username):    # this function is called in the main thread
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    print(f"Connecting to server {server_addr}:{server_port}")
    client_socket.sendto(f"JOIN {username}".encode(), (server_addr, server_port))   # send JOIN message to server

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))   # create thread to receive messages from server
    receive_thread.start()

    while True: # loop to send messages to server
        message = input(f"{username}: ")
        if message == "exit":   # if message is exit, send LEAVE message to server and break from loop
            client_socket.sendto("LEAVE".encode(), (server_addr, server_port))
            break
        client_socket.sendto(f"{username}: {message}".encode(), (server_addr, server_port))  # send message to server

    client_socket.close()

# Main Code
if __name__ == "__main__":
    server_addr = '127.0.0.1'
    server_port = 9301

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Enter your username: ")

    run(server_addr, server_port, username)