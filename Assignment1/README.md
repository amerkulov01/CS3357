# Simple Web Application Project
This project demonstrates a basic web application setup with a Python-based server (server.py), a client (client.py), and a simple HTML page (hello.html). The server serves the HTML page, which can be requested by the client.

## Project Structure
- server.py: The Python script that runs the server, listening for incoming requests and serving the hello.html page.
- client.py: The Python client that sends a request to the server to retrieve the hello.html page.
- hello.html: A simple HTML page that is served by the server upon request.
## Getting Started
### Prerequisites
- Python 3.x installed on your machine.
### Running the Server
- To start the server, open a terminal and run:
```
python server.py
```
- This will start the server, making it listen for incoming requests on a predefined port (update with the actual port if specified in server.py).

### Running the Client
- With the server running, open a new terminal window and execute:

```
python client.py
```
- This sends a request to the server to fetch the hello.html page, which should then be displayed in the terminal or handled according to the logic defined in client.py.

## Features
- Simple Server: A Python server that listens for requests and serves an HTML page.
- Client-Server Communication: Demonstrates basic client-server communication over HTTP.
- HTML Content: Serves a simple HTML document that can be expanded upon for more complex web development learning.
