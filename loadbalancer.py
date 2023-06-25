import socket
import time

HOST= "10.0.0.1"
PORT= 80

SERVER1= "192.168.0.101"
SERVER2= "192.168.0.102"
SERVER3= "192.168.0.103"
RESPOND_SIZE=2

def handle_m(conn, data):
    s1= socket.socket()
    s1.connect((SERVER1,PORT))
    s1.send(data.encode())
    sent= time.time()
    response = s1.recv(RESPOND_SIZE)
    recieved=time.time()
    conn.send(response)
    s1.close()

if __name__ == '__main__':
    s= socket.socket()
    s.bind((HOST,PORT))
    while True:
        s.listen()
        conn , addr = s.accept()
        data= conn.recv(2).decode()

        if data[0]=='M':
            handle_m(conn, data)
        elif data[0]=='P':
            handle_m(conn, data)
        elif data[0]=='V':
            handle_m(conn, data)

        conn.close()

    s.close()