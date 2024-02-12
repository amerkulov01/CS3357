# Andrei Merkulov, 251145994
# CS 3357, Assignment 4
# 2023-12-10

import threading
import numpy as np
import pygame 
from network import Network
import time
import re

width = 500
height = 500
rows = 20 

clients = []

rgb_colors = {
    "red" : (255, 0, 0),
    "green" : (0, 255, 0),
    "blue" : (0, 0, 255),
    "yellow" : (255, 255, 0),
    "orange" : (255, 165, 0),
} 
rgb_colors_list = list(rgb_colors.values())

def drawGrid(w, surface):
    global rows
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y +sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x, 0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0, y),(w,y))

def drawThings(surface, positions, color = None, eye = False):
    global width, rgb_colors_list
    dis = width // rows
    if color is None : 
        color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
    for pos_id, pos in enumerate(positions):
        i, j = pos

        pygame.draw.rect(surface, color , (i*dis+1,j*dis+1,dis-2,dis-2))
        if eye and pos_id == 0:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

def draw(surface, players, snacks):
    global rgb_colors_list

    surface.fill((0,0,0))
    drawGrid(width, surface)
    for i, player in enumerate(players) : 
        color = rgb_colors_list[i % len(rgb_colors_list)]
        drawThings(surface, player, color = color, eye = True) 
    drawThings(surface, snacks, (0, 255, 0))
    pygame.display.update()

def listen_for_messages(network):   # receive from server
    messageLength = network.client.recv(3).decode()
    if(messageLength.isdigit() == True):    # if messageLength is a number
        data = network.client.recv(int(messageLength)).decode() #conn.recv
        print(data)
        if(data == "Congratulations"):
            print(data)
        else:
            return None
    else:
        return None
            
def main():
    
    win = pygame.display.set_mode((width,height))   # set up window
    n = Network()
    flag = True
    
    while flag: # main loop
        
        events = pygame.event.get()     # get events
        pos = None 
        if len(events) > 0 :    # if there are events
            
            for event in events : 
                if event.type == pygame.QUIT:   # if the event is quit
                    flag = False
                    pos = n.send("004quit", receive=True)   # send quit message to server
                    pygame.quit()
                if event.type == pygame.KEYDOWN:    # if the event is a key press
                    if event.key == pygame.K_LEFT:  # if the key is left
                        pos = n.send("005left", receive = True)
                    elif event.key == pygame.K_RIGHT:   # if the key is right
                        pos = n.send("005right", receive = True)
                    elif event.key == pygame.K_UP:  # if the key is up
                        pos = n.send("002up", receive = True)
                    elif event.key == pygame.K_DOWN:    # if the key is down
                        pos = n.send("004down", receive = True)
                    elif event.key == pygame.K_SPACE:   # if the key is space
                        pos = n.send("005reset", receive = True)
                    elif event.key == pygame.K_z:   # if the key is z
                        pos = n.send("016Congratulations!", receive = False)
                    elif event.key == pygame.K_x:   # if the key is x
                        pos = n.send("009It works!", receive = False)
                    elif event.key == pygame.K_c:   # if the key is c
                        pos = n.send("006Ready?", receive = False)
                
                
        else : 
            pos = n.send("003get", receive = True)  # send get message to server
            if (pos is not None):
                if ('Congratulations!' in pos or 'It works!' in pos or 'Ready?' in pos):    # if the message is a message
                    print(pos)
        
        snacks, players = [], []
        if pos is not None and "|" in pos: 
            raw_players = pos.split("|")[0].split("**")
            raw_snacks = pos.split("|")[1].split("**")

            if raw_players == '' : 
                pass 
            else : 
                for raw_player in raw_players :
                    raw_positions = raw_player.split("*")
                    if len(raw_positions) == 0 :
                        continue
                    
                    positions = []
                    for raw_position in raw_positions :
                        if raw_position == "" :
                            continue
                        nums = raw_position.split(')')[0].split('(')[1].split(',')
                        positions.append((int(nums[0]), int(nums[1])))
                    players.append(positions)


            if len(raw_snacks) == 0 :
                continue

            for i in range(len(raw_snacks)) :
                nums = raw_snacks[i].split(')')[0].split('(')[1].split(',')
                snacks.append((int(nums[0]), int(nums[1])))
            

        draw(win, players, snacks)
    

if __name__ == "__main__":
    main()
