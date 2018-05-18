#This is for the client

import socket # Imports the socket module

s = socket.socket() # Create a socket object
HOST = "127.0.0.1"
PORT = 1925

s.connect((HOST, PORT))
print (s.recv(1024))
s.close # Simply closes the socket when done
