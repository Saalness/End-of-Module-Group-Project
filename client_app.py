"""This is the client's side which connects to the server 
in the local IP address and then sends a message
"""

import socket                               # Import socket module
import main
from main import picked, enc, encrypt_file  # Config variables to use in functions


s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)             # Create a socket object     
port = 60000                                      # Reserve a port for your service.
host = "127.0.0.1"
format = "utf-8"
size = 1024

try:
    s.connect((host, port))
except ConnectionRefusedError:
    print("There is a problem with the connection.")
s.send(("Connection Established").encode())

# Dictionary Definition and population ie Fruits,Vegetables and Nuts as store items
dataDict = {'Store Items': ['Fruits', 'Vegetables', 'Nuts'], 'Fruits': {'Mango': 6, 'Orange': 3, 'Apple': 50, 'Grapes': 15}, 'Vegetables': {
        'Sweet potatoes': 100, 'Spinach': 20, 'Carrot': 18}, 'Nuts': {'Almonds': 10, 'Cashews': 5, 'Walnuts': 150, 'Peanuts': 80}}

# Serialize the dictionary
serialised_dict = main.pickling_choice(picked, dataDict)
s.send(serialised_dict.encode())

def send_choice():
    print("""-----------------------Menu--------------------

      --> 1 ----> Send Dictionary

      --> 2 ----> Send Text file""")

    opt = int(input("Select option :"))
    if opt == 1:
       s.send(serialised_dict.encode())
       """ for key in dataDict.keys():
                s.send(str(dataDict[key]).encode())
                print('Sent ', repr(dataDict[key]))
                """
    elif opt == 2:
        # create file
        filename = 'textfile.txt'
        with open(filename, 'w+') as file:
            file.write("This text file was created by the client app")
            try:
                encrypt_file(filename)
                s.send(file.read(size).encode())
            except TypeError:
                print("There was a problem sending the file.")
            file.close()
        print('Successfully sent the file')
    else:
        print("Please try typing in 1 or 2")
        send_choice()
s.close()
print('connection closed')