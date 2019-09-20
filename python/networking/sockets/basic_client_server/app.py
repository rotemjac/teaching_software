import _thread
import time

from server import server
from client import client

print(" ------------------------------------------ ")
print("Welcome to the Socket Client-Server program")
print(" ------------------------------------------ ")

PORT = 8080

# -------------------- Bring Server up and make client connect to it ---------------- #
socketServer = server.SocketServer()
socketServer.start(PORT)

socketClient = client.SocketClient()
socketClient.connect_to_server('127.0.0.1', PORT)

# -------------------- Start communication ---------------- #

# We are using threads here because inisde start_excepting_requests there is
# the server_sock.accept() method which is a blocking method
_thread.start_new_thread(socketServer.start_excepting_requests, ())

stopProgram = False
while stopProgram is False:
    message = input("Please enter a message for the socket server: ")
    socketClient.send_message_to_server(message)

    msgFromServer = socketClient.get_message_from_server()
    print(msgFromServer.decode())

    if message == "CLOSE_CONNECTION":
        socketClient.close_connection()
        stopProgram = True
        print("GoodBye!!")



