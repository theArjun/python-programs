import socket

# Here AF.INET refers to the ipv4 connection and SOCK_STREAM refers to the TCP/IP connection.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 6666 is my desired port number for connection and gethostname returns the localhost.
serversocket.bind((socket.gethostname(), 6666))
# Here 5 refers to the queue limit of socket communication.
serversocket.listen(5)

while True:

    # Returns the hostaddress and the port in address.
    clientsocket, address = serversocket.accept()
    print(f"Connection from {address} has been established !")
    # First parameter is the bytestream of the message and second is the encoding standard.
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    # Always a good practice to close the connection.
    clientsocket.close()
