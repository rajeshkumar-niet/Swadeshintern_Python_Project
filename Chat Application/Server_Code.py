import socket
import threading

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
host = '127.0.0.1'  # Use your host IP or '127.0.0.1' for localhost
port = 12345  # Use a port number that is not already in use

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {host}:{port}")

# Lists to hold client connections and their names
clients = []
client_names = []

# Function to broadcast messages to all clients
def broadcast(message, sender_name):
    for client in clients:
        if client != sender_name:
            try:
                client.send(message)
            except:
                client.close()
                remove_client(client)

# Function to handle each client
def handle_client(client_socket):
    name = client_socket.recv(1024).decode('utf-8')
    client_names.append(name)
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"{name}: {message.decode('utf-8')}")
                broadcast(f"{name}: {message}".encode('utf-8'), client_socket)
        except:
            continue

# Function to remove a client from the lists
def remove_client(client_socket):
    index = clients.index(client_socket)
    clients.remove(client_socket)
    client_socket.close()
    name = client_names[index]
    client_names.remove(name)
    broadcast(f"{name} has left the chat.".encode('utf-8'), None)

# Accept and handle client connections
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Connected to {client_address[0]}:{client_address[1]}")
    client_socket.send("Welcome to the chat room! Please enter your name:".encode('utf-8'))
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
