"""This is the client's side which connects to the server 
in the local IP address and then sends a message
it includes:

parameters definition: -pickling format
                   -to encrypt the file or not

default variables for pickling and encryption preferences




dictionary is created and populated


pickling config chosen


dictionary is serialised


text file is created


encryption config chosen

(text file is encrypted in config if needed?)






send the dictionary + text file to the server


"""

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print ('file opened')
    dat=[]
    while True:
        
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        dat.append(data)
        if not data:
            break
        # write data to a file
        f.write(data)


f.close()
print('Successfully get the file')
s.close()
print('connection closed')