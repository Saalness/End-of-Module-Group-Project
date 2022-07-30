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


#below is the choice of the pickling format
rxdic = dict
dat=[]
for i in range(len(dat)):
        rxdic[str(i)]=dat[i]
def pickling_choice(picked):
    if picked == 'pickle':
        file = open("file1.txt","wb")
        data_serialised = pickle.dump(rxdic,file)
        file.close()
    elif picked == 'json':
        data_serialised = json.dumps(rxdic) #!!!!!!!!!!!!! ERROR this is not data serialisable
    elif picked == 'xml':
        data_serialised = dict2xml(rxdic)
    return data_serialised    

def enc_check(enc, text_file):
    if enc == 'true':
        encrypt_file(text_file)   
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!this is not called yet

#the encryption / decryption functions
def encrypt_file(text_file):

    #string is read from text file (parameter might need to be changed)
    with open(text_file, 'w+') as line:
        file = line.readline()
    encLine = fernet.encrypt(file.encode())
    return encLine

    #!!!!encrypted line needs to replace the line in the text file (or a new text file is made?)

def decrypt_file(text_file):
    #read first line from file
    line = "first line to decrypt"

    decLine = fernet.decrypt(line).decode()
    return decLine

    #!!!!encrypted line needs to replace the line in the text file --

#whether to print to screen or text file
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