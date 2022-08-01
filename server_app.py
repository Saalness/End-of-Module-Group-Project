"""This is the server's side which runs forever, it listens to the IP address 
of the same machine, connects to it, it waits for the client to send data

if text file is encrypted, it is decrypted it
calls function to print the text file or dictionary
"""
import socket
from main import enc, decrypt_file, print_output #config variables to use in functions

# take the port name
port = 60000
host = "127.0.0.1"
# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
# bind the socket with server
# and port number
s.bind((host, port))
# allow maximum 1 connection to
# the socket
s.listen(5)
# wait till a client accept
# connection
while True:
    c, addr = s.accept()
    # display client address
    print("CONNECTION FROM:", str(addr))
    #open recieved file to write contents sent by client
    with open('received_file.txt', 'wb') as f:
        print('file opened')
        dat = []
        while True:  #recieves data from client
            print('receiving data...')
            data = c.recv(1024)
            print_output(data)
            dat.append(data.decode())
            if not data:
                break
            # write data to a file
            f.write(data)  
    # disconnect the server
    c.close()
