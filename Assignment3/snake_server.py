# Andrei Merkulov, 251145994
# CS 3357, Assignment 4
# 2023-12-10

import numpy as np
import socket
from _thread import *
import pickle
from snake import SnakeGame
import uuid
import time 
import threading

# server = "10.11.250.207"
server = "localhost"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Client():
    def __init__(self):
        self.conn, self.addr = s.accept()
        

counter = 0 
rows = 20 

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
# s.settimeout(0.5)
print("Waiting for a connection, Server Started")


game = SnakeGame(rows)
game_state = "" 
last_move_timestamp = time.time()
interval = 0.2
moves_queue = set()

clients = []

def game_thread() : 
    global game, moves_queue, game_state 
    while True :
        last_move_timestamp = time.time()
        game.move(moves_queue)
        moves_queue = set()
        game_state_length = len(game.get_state())
        game_state = game.get_state()
        game_state = f"{game_state_length:003}" + game_state
        while time.time() - last_move_timestamp < interval : 
            time.sleep(0.1) 



rgb_colors = {
    "red" : (255, 0, 0),
    "green" : (0, 255, 0),
    "blue" : (0, 0, 255),
    "yellow" : (255, 255, 0),
    "orange" : (255, 165, 0),
} 
rgb_colors_list = list(rgb_colors.values())

def out(message): # send to all clients
    for client in clients:
        client.send(message.encode())
        print("sent" + message + "to " + str(client))

def client_thread(conn, unique_id): # receive from client
    global game, counter

    color = rgb_colors_list[np.random.randint(0, len(rgb_colors_list))]
    game.add_player(unique_id, color = color) 
    start_new_thread(game_thread, ())
    
    while True :    
        messageLength = conn.recv(3).decode()   
        data = conn.recv(int(messageLength)).decode() #conn.recv
        conn.send(game_state.encode()) #conn.send
        
        move = None 
        if not data :   
            print("no data received from client")
            break 
        elif data == "get" :    # get game state
            pass 
        elif data == "quit" :   # quit game
            print("received quit")
            game.remove_player(unique_id)
            break
        elif data == "reset" :  # reset game
            game.reset_player(unique_id)

        elif data in ["up", "down", "left", "right"] :  # move
            move = data
            moves_queue.add((unique_id, move))
        elif data in ["Congratulations!", "It works!", "Ready?"] :  # message
            length = 20 + int(messageLength)    # 20 is the length of the message
            length = f"{length:003}"        # 3 is the length of the length
            out(length+str(conn.getpeername())+data)    # send to all clients
        else :
            print("Invalid data received from client:", data)

    conn.close()

def main() : 
    global counter, game

    while True: 
        conn, addr = s.accept() 
        clients.append(conn)    # add client to list of clients
        print("Connected to:", addr)    
        unique_id = str(uuid.uuid4())   # generate unique id
        threading.Thread(target=client_thread, args=(conn, unique_id)).start()  # start thread for client

if __name__ == "__main__" : 
    main()