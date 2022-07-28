#This is the configuration file which uses if statements to check the passed parameters from the client's side

from cryptography.fernet import Fernet
from dict2xml import dict2xml
import json
import pickle

#instance of Fernet class created and key generated here
key = Fernet.generate_key()

fernet = Fernet(key)



#below is the choice of the pickling format
rxdic=dict
for i in range(len(dat)):
        rxdic[str(i)]=dat[i]
pic=int(input("""Please select the pickling format:
                  1-> binary 
                  2-> JSON
                  3-> XML"""))
if pic==1:
    f1=open("file1.txt","wb")
    pickle.dump(rxdic,f1)
    f1.close()
elif pic==2:
    b = json.loads(rxdic)
elif pic==3:
    xml = dict2xml(rxdic)

#the encryption / decryption functions
def encrypt_file(text_file):

    #!!!!string needs to be read from text file (parameter might need to be changed) + loop until all lines are done?
    line = "first line of file - TO BE CHANGED"

    encLine = fernet.encrypt(line.encode())
    return encLine

    #!!!!encrypted line needs to replace the line in the text file (or a new text file is made?)

def decrypt_file(text_file):
    #read first line from file
    line = "first line to decrypt"

    decLine = fernet.decrypt(line).decode()
    return decLine

    #!!!!encrypted line needs to replace the line in the text file --


#whether to print to screen or text file