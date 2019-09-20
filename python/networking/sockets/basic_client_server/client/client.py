import socket

class SocketClient:

    def __init__(self):
        # Create socket object
        self.client_sock = socket.socket()


    def connect_to_server(self,ip, port):
        # listen on port 8080 to everybody(0.0.0.0. means everybody in the network/subnet that connects)
        self.client_sock.connect((ip, port))

    def send_message_to_server(self,message):
        self.client_sock.send(message.encode())

    def get_message_from_server(self):
        # Receive the message from server
        return self.client_sock.recv(1024)

    def close_connection(self):
        print("Closing client socket...")
        self.client_sock.close()

