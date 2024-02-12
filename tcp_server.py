import socket
import select
import threading

HOST = '127.0.0.1'
PORT = 9301
BUFFER_SIZE = 1024

def broadcast_message(message, sender_socket):  # broadcast message to all clients except the sender
    for client_socket in client_list:   # iterate through all connected clients
        if client_socket != server_socket and client_socket != sender_socket:   
            try:    # attempt to send message to client
                client_socket.send(message)
            except:
                client_socket.close()
                client_list.remove(client_socket)

def client_thread(client_socket, client_address):   # this function is called in a separate thread for each connected client
    client_socket.send(b'Welcome to the chatroom!\n')
    while True: # loop to receive messages from client
        try:    # attempt to receive message from client
            message = client_socket.recv(BUFFER_SIZE)
            if message: # if message is not empty
                broadcast_message(message, client_socket)
            else:
                raise Exception('Client disconnected')
        except:
            client_socket.close()
            client_list.remove(client_socket)   # remove client from client list
            return

if __name__ == '__main__':  # this is the main thread
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create TCP socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # set socket option to reuse address
    server_socket.bind((HOST, PORT))    # bind socket to address
    server_socket.listen(10)    # listen for connections

    client_list = [server_socket]   # list of connected clients

    print(f'Server started on {HOST}:{PORT}')

    while True: # loop to accept connections from clients
        read_sockets, _, _ = select.select(client_list, [], []) # wait for activity on any of the sockets
        for sock in read_sockets:   # iterate through sockets with activity
            if sock == server_socket:   # if activity is on server socket, accept connection
                client_socket, client_address = server_socket.accept()
                client_list.append(client_socket)
                print(f'Client {client_address} connected')
                threading.Thread(target=client_thread, args=(client_socket, client_address)).start()
            else:
                pass