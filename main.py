#This is the configuration file which uses if statements to check the passed parameters from the client's side
from cryptography.fernet import Fernet
import json
import pickle
from config import myconfig
from dict2xml import dict2xml

#values taken from the config file
picked = myconfig["pickling"]
enc = myconfig["encryption"]
print_type = myconfig["printing"]
#instance of Fernet class created and key generated here
key = Fernet.generate_key()
fernet = Fernet(key)
def pickling_choice(picked, dict):
    """depending on the choice of the pickling format, the dictionary is serialised"""
    #dat=[]
    #for i in range(len(dat)):
     #   dict[str(i)] = dat[i]
    if picked == 'pickle':
        file = open("file1.txt","wb")
        data_serialised = pickle.dump(dict, file)
        file.close()
    elif picked == 'json':
        data_serialised = json.dumps(dict)
        f1 = open("file2.json", "wb")
        pickle.dump(str(data_serialised).encode(), f1)
        f1.close()
    elif picked == 'xml':
        data_serialised = dict2xml(dict)
        f1 = open("file3.xml", "wb")
        pickle.dump(str(data_serialised).encode(), f1)
        f1.close()
    print(data_serialised)  
    return data_serialised    
#the encryption / decryption functions
def encrypt_file(text_file):
    """opens file, reads line to encrypt then writes the encrypted line"""
    #string is read from text file
    with open(text_file, 'w+') as line:
        try:
            file = line.readline()
            encLine = fernet.encrypt(file.encode())
        except TypeError:
            "Encryption was not successful"
        line.write(encLine.decode())
    line.close()
    print("Encrypted line: ", encLine)
    return encLine
def decrypt_file(contents):
    """decrypts the line"""
    with open('recieved_file.txt', 'w') as line:
                line.write(contents)
                file = line.readline()
                decLine = fernet.decrypt(file).decode()
    return decLine
def print_output(data):
    """option to print on screen or in a file"""
    try:
        if print_type == "screen":
            print("Output data = ", data)
        elif print_type == "file":
            with open('recieved_file.txt', 'w') as file:
                file.write(data)
    except FileNotFoundError:
        print("File was not found")