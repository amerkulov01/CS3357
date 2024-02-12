# Assignment: UDP Simple Chat Room - UDP Server Code Implementation

# Libraries and Imports
import socket

# Global Variables
RECV_BUFFER = 4096

# Function Definitions
def run(server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # set socket option to reuse address
    server_socket.bind(('127.0.0.1', server_port))  # bind socket to address

    print(f"Server started on port {server_port}")

    clients = {}

    while True: # loop to receive messages from clients
        data, addr = server_socket.recvfrom(RECV_BUFFER)
        message = data.decode()

        if message.startswith("JOIN"):  # if message is JOIN message
            username = message.split()[1]
            clients[addr] = username
            print(f"Client {username} ({addr[0]}:{addr[1]}) joined the chat room")
            broadcast(server_socket, f"Client {username} joined the chat room", clients)    # broadcast message to all clients
        elif message == "LEAVE":    # if message is LEAVE message
            username = clients[addr]
            del clients[addr]
            print(f"Client {username} ({addr[0]}:{addr[1]}) left the chat room")
            broadcast(server_socket, f"Client {username} left the chat room", clients)  # broadcast message to all clients
        else:
            username = clients[addr]
            message = message.split(': ', 1)
            if len(message) > 1:
                message = f"{username}: {message[1]}"
                print(f"Received message from {username} ({addr[0]}:{addr[1]}): {message}")  # print message locally
                broadcast(server_socket, message, clients)  # broadcast message to all clients

    server_socket.close()

def broadcast(server_socket, message, clients): # broadcast message to all clients
    for client in clients:
        server_socket.sendto(message.encode(), client)

# Main Code
if __name__ == "__main__":
    server_port = 9301

    run(server_port)