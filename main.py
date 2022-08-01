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
    dat=[]
    for i in range(len(dat)):
        dict[str(i)] = dat[i]
    if picked == 'pickle':
        file = open("file1.txt","wb")
        data_serialised = pickle.dump(dict,file)
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
        except FileNotFoundError:
            "Encryption was not successful"
        file.write(encLine)
    line.close()
def decrypt_file(text_file):
    """opens file, reads line to decrypt then writes the decrypted line"""
    #read line from file
    line = "first line to decrypt"
    with open(text_file, 'w+') as line:
        file = line.readline()
        decLine = fernet.decrypt(file).decode()
        line.write(decLine)
    line.close()
def print_output(type, data):
    """option to print on screen or in a file"""
    try:
        if type == "screen":
            print(data)
        elif type == "file":
            with open('recieved_file.txt', 'w') as file:
                file.write(data)
    except FileNotFoundError:
        print("File was not found")