# Multiplayer Snake Game
This project is a Python implementation of the classic Snake game with a twist: it supports networked multiplayer functionality. Players can connect to a server to play the Snake game, controlling their own snake and competing or cooperating with others in real-time.

## Project Structure
- snake.py: The core game logic for the Snake game, including snake movement, food spawning, and collision detection.
- network.py: Handles the networking aspect, providing functionality to connect, send, and receive game state updates.
- snake_client.py: The client-side script that players run to connect to the game server, rendering the game state and sending player inputs.
- snake_server.py: The server-side script that manages the game state, processes inputs from clients, and sends updates to all connected players.
## Getting Started
### Prerequisites
- Python 3.x
### Installation
- Clone this repository or download the ZIP file and extract it to your local machine.
- Ensure Python 3.x is installed on your system.
## Running the Server
- Open a terminal or command prompt.
- Navigate to the project directory.
- Start the game server by running:
```
python snake_server.py
```
### Connecting as a Player
- Open a new terminal or command prompt window.
- Navigate to the project directory.
- Start a client instance by running:
```
python snake_client.py
```

- Use the arrow keys to control your snake.
- Eat food to grow longer and score points.
- Avoid colliding with walls or other snakes.
### Connecting another Player
- Run the same command in a different terminal:
```
python snake_client.py
```
- Compete against or cooperate with other players connected to the server.
## Features
- Multiplayer support over a network.
- Real-time snake movement and food spawning.
- Collision detection and game over logic.
- Dynamic game state updates across all clients.
