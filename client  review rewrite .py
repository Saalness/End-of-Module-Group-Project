import json

import socket                   # Import socket module

from dict2xml import dict2xml

import pickle                       # Import socket module


s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)             # Create a socket object

host = "127.0.0.1"  # socket.gethostname()     #  Get local machine name

port = 50023                    # Reserve a port for your service.


s.connect((host, port))

s.send(("Hello server!").encode())


with open('received_file.txt', 'wb') as f:

    print('file opened')

    dat = []

    while True:

        print('receiving data...')

        data = s.recv(1024)

        print('data=%s', (data))

        dat.append(data.decode())

        if not data:

            break

        # write data to a file

        f.write(data)

rxdic = dict()
print(dat)
for i in range(len(dat)):

    rxdic[str(i)] = dat[i]

pic = int(input("""Please select the pickling format:

                  1-> binary 

                  2-> JSON

                  3-> XML   """))

if pic == 1:

    binD = ' '.join(format(ord(x), 'b') for x in rxdic)
    print("Output   :  " + binD)

    f1 = open("file1.txt", "wb")
    pickle.dump(binD.encode(), f1)
    f1.close()

elif pic == 2:
    b = json.dumps(rxdic)
    print("Output   :  " + b)

    f1 = open("file2.json", "wb")
    pickle.dump(str(b).encode(), f1)
    f1.close()

elif pic == 3:
    xml = dict2xml(rxdic)
    print("Output   :  " + xml)

    f1 = open("file3.xml", "wb")
    pickle.dump(str(xml).encode(), f1)
    f1.close()


f.close()

print('Successfully get the file')

s.close()

print('connection closed')
