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
import main
from main import picked, enc, print_type
from config import myconfig

s = socket.socket()             # Create a socket object     
port = 60000                    # Reserve a port for your service.
format = "utf-8"
size = 1024
try:
    s.connect(('127.0.0.1', port))
except ConnectionRefusedError:
    print("There is a problem with the connection.")
s.send(b"Connection Established")

dataDict = {}  # Dictionary Definition

# Populate the dictionary ie Fruits,Vegetables and Nuts as store items
dataDict = {'Store Items': ['Fruits', 'Vegetables', 'Nuts'], 'Fruits': {'Mango': 6, 'Orange': 3, 'Apple': 50, 'Grapes': 15}, 'Vegetables': {
        'Sweet potatoes': 100, 'Spinach': 20, 'Carrot': 18}, 'Nuts': {'Almonds': 10, 'Cashews': 5, 'Walnuts': 150, 'Peanuts': 80}}

# Serialize the dictionary
serialised_dict = main.pickling_choice(picked)
s.send(serialised_dict.encode())
    
# create file

with open('textfile.txt', 'w+') as file:
    file.write("This text file was created by the client app")
    s.send(file.read())
    
file.close()
print('Successfully sent the file')
s.close()
print('connection closed')