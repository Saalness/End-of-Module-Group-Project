"""This is the server's side which runs forever, it listens to the IP address 
of the same machine, connects to it, it waits for the client to send data

-default variable - prints on screen or null
printing on screen or in text file choice
if text file is encrypted, needs to decrypt it (here or in config?)
calls function to print the text file


"""
import socket
import main
from main import picked, enc, print_type

# take the port name
port = 60000
# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('127.0.0.1', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
while True:
    c, addr = s.accept()

    # display client address
    print("CONNECTION FROM:", str(addr))

#!!!!!!!!!needs to recieve text file after connection is made
    
    # disconnect the server
    c.close()
