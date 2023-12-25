import socket

SERVER = "localhost"
PORT = 4221
client = socket.socket()  # defaults work
client.connect((SERVER, PORT))
client.send("hello from client".encode())  # utf-8 is default
print(client.recv(1024).decode())
