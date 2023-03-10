
from http import server
import socket
s = socket.socket()

s.bind(('127.0.0.1', 65230))
s.listen(5)
print("waiting for connections")
while True:
    c, addr= s.accept()
    print("connected with ", addr)
    print(c.recv(1024).decode())
    print('\n')
    print("NAME OF THE CUSTOMER IS : " + c.recv(1024).decode())
    print("TOTAL BILL : " + c.recv(1024).decode() +"")
    print("CONTACT INFO OF CUSTOMER : " + c.recv(1024).decode() +"")
    print("BILL NO           : " + c.recv(1024).decode() +"")

