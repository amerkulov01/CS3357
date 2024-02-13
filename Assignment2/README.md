# Python TCP/UDP Client-Server Communication Project
This project showcases basic network communication using both TCP and UDP protocols in Python. It consists of separate scripts for TCP and UDP servers and clients, demonstrating how to establish connections, send messages, and receive responses between clients and servers.

## Project Structure
- tcp_server.py: A TCP server that listens for connections from TCP clients.
- tcp_client.py: A TCP client that connects to the TCP server and exchanges messages.
- udp_server.py: A UDP server that listens for messages from UDP clients.
- udp_client.py: A UDP client that sends messages to the UDP server.
## Getting Started
### Prerequisites
- Python 3.x
### Running the TCP Server:
- Start the TCP Server: Open a terminal and run:
```
python tcp_server.py
```
- This will start the TCP server, which will listen for incoming connections.

### Run the TCP Client: 
- Open a new terminal and run:
```
python tcp_client.py
```
- This will start the TCP client, which will connect to the server and allow you to send messages.

### Running the UDP Server:
- Start the UDP Server: Open a terminal and run:
```
python udp_server.py
```
- This will start the UDP server, which will listen for messages.

### Run the UDP Client: 
- Open a new terminal and run:
```
python udp_client.py
```
- This will start the UDP client, which will send messages to the server.

## Features
- TCP Communication: Demonstrates how to establish a persistent connection between a client and server, allowing for a two-way exchange of messages.
- UDP Communication: Shows how to send messages from a client to a server without establishing a persistent connection, suitable for cases where speed is more critical than reliability.
- Basic Networking Concepts: Provides a practical example of networking concepts such as sockets, ports, and IP addresses.
