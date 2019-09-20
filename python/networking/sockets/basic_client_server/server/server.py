import socket

class SocketServer:

    def __init__(self):
        # Create socket object
        self.server_sock = socket.socket()

    def start(self,port):

        # listen on port 8080 to everybody(0.0.0.0. means everybody in the network/subnet that connects)
        self.server_sock.bind(('0.0.0.0', port))

        # Allow only one connection to wait without being handled by accept
        self.server_sock.listen(1)

    def start_excepting_requests(self):
        # Accept is a blocking method - code wil freeze and wait for a connection
        # when a connection arrives, the 'accept' method will return a tuple
        # with two items - one is the socker object for the client, and the 2nd is the client's IP address
        (socket_with_client, client_address) = self.server_sock.accept()

        # We need a loop here in order to return always to the "socket_with_client.recv" line
        # and not wait only one time for messages to come
        # if you work without the while loop - after one message from the socket client
        # the server will stop listening (with socket_with_client.recv)
        shutdown_server = False
        while shutdown_server is False:
            # From the client socket object - get the message which arrived
            # notice that recv is a blocking method and waits for a message from the other
            # side of the socket
            message = socket_with_client.recv(1024).decode()
            if message == "CLOSE_CONNECTION":
                socket_with_client.send("Closing server and server socket...".encode())
                socket_with_client.close()
                self.server_sock.close()
                shutdown_server = True
            else:
                socket_with_client.send(("Thanks, I got your message of: " + message).encode())



