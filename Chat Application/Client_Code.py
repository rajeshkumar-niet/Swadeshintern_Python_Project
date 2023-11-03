import socket
import threading

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port to connect to
host = '127.0.0.1'  # Use the server's IP or '127.0.0.1' for localhost
port = 12345  # Use the same port as the server

# Connect to the server
client_socket.connect((host, port))

# Get the client's name
name = input("Enter your name: ")
client_socket.send(name.encode('utf-8'))

# Function to send messages to the server
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            print("An error occurred.")
            client_socket.close()
            break

# Start threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_messages)

send_thread.start()
receive_thread.start()
