import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting socket to the desired address and the port.
clientsocket.connect((socket.gethostname(), 6666))
# Buffer size for storing the byte message.
# Buffer size also can be reduced but full transmission may not be guaranteed,
# So looping the receving side is essential.
msg = clientsocket.recv(1024)
# Decoding the message using UTF-8 Standard.
print(msg.decode("utf-8"))
