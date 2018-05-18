#This is for the server

from socket import *
from time import ctime
from threading import Thread

class ClientHandler(Thread):
    """Handles a client request"""
    def __init__(self, client):
        Thread.__init__(self)
        self_client = client

    def run(self):
        self._client.send(bytes(c_time + ' Have a nice day!', 'ascii'))
        self._client.close()

HOST = "127.0.0.1"
PORT = 1925
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
# The server now just waits for connections
#and hands over sockets to client handlers
while True:
    print('Waiting for connection')
    client, address = server.accept()
    print('...connected from:', address)
    handler = clientHandler(client)
    handler.start()
    
