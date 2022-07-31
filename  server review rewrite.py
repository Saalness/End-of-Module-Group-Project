

import json
import socket                   # Import socket module

# Import socket module


port = 50023                    # Reserve a port for your service.

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)             # Create a socket object

host = ""  # socket.gethostname()     # Get local machine name

s.bind((host, port))            # Bind to the port

s.listen(1)                     # Now wait for client connection.


print('Server listening....')


print("""-----------------------Menu--------------------

      --> 1 ----> Send Dictionary

      --> 2 ----> Send Text file""")

opt = int(input("Select option :"))

if opt == 1:
    dataDict = {}  # Dictionanry Definition

    # Dictionary population
    dataDict = {
        'Name': 'Store Name',
        'StoreItems': ['Fruits', 'Vegetables', 'Nuts'],
        'Fruits': {'Mango': 6, 'Orange': 3, 'Apple': 50, 'Grapes': 15},
        'Vegetables': {'Sweet potatoes': 100, 'Spinach': 20, 'Carrot': 18},
        'Nuts': {'Almonds': 10, 'Cashews': 5, 'Walnuts': 150, 'Peanuts': 80}
    }

    #txdic = dict()

    #siz = int(input("Enter the population of dictionary :"))

    # for i in range(siz):

    #    txdic[str(i)] = i

    print(dataDict)
    while True:

        conn, addr = s.accept()     # Establish connection with client.

        print('Got connection from', addr)

        data = conn.recv(1024).decode()

        print('Server received', repr(data))

        for key in dataDict.keys():

            conn.send(str(dataDict[key]).encode())

            print('Sent ', repr(dataDict[key]))

        print('Done sending')

       # conn.send(('Thank you for connecting').encode())

        conn.close()

elif opt == 2:

    filename = 'file_1.txt'

    f = open(filename, 'rb')

    l = f.read(1024)

    dat = []

    while (l):
        conn, addr = s.accept()     # Establish connection with client.
        conn.send(l)

        print('Sent ', repr(l))

        l = f.read(1024)

    f.close()

    print('Done sending')

    conn.send('Thank you for connecting')

    conn.close()
