"""This is the server's side which runs forever, it listens to the IP address 
of the same machine, connects to it, it waits for the client to send data

-default variable - prints on screen or null

printing on screen or in text file choice


if text file is encrypted, needs to decrypt it (here or in config?)


calls function to print the text file


"""

import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

print("""-----------------------Menu--------------------
      --> 1 ----> Send Dictionary
      --> 2 ----> Send Text file""")
opt=int(input("Select option :"))
if  opt==1:
    txdic=dict
    siz=int(input("Enter the population of dictionary :"))
    
elif opt==2:
    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    dat=[]
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)

for i in range(siz):
    txdic[str(i)]=i
while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    
    for i in txdic.keys:
        conn.send(txdic[i])
        print('Sent ',repr(txdic[i]))
    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()

    f.close()
    
    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()
      
   