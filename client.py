import socket
import os

HEADER = 64
#PORT = 5050
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)


def file(SERVER, PORT, filename):
    ADDR = (SERVER, PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    #client.send(sendsize)
    #client.send(msg)
    f = open(filename,"rb")
    size = os.stat(filename).st_size
    print("File size: "+str(size)+" bytes")
    file = f.read(1024)
    while file:
        client.send(file)
        file = f.read(1024)
    client.shutdown(socket.SHUT_WR)
    print("File is sent")