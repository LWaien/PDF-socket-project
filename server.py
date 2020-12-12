import socket
#HEADER = 64

def handle_file(conn):
    src = conn.recv(1024).decode('utf-8')
    #len = conn.recv(HEADER).decode('utf-8')
    #len = int(len)
    #fname = str(src.decode('utf-8'))
    #print("file: " + fname)
    #path = fname.split('/')
    file = open(path[-1] ,'wb')
    while src:
        file.write(src)
        src = conn.recv(1024)
    conn.close()
    print("File recieved")


def start(PORT):
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"server is listening on {SERVER}:{PORT}")
    conn, addr = server.accept()


    print(f"{addr} connected.")


    handle_file(conn)



