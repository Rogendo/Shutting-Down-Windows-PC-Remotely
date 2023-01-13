import socket
import sys
import os
import time


s=socket.socket()
host="192.168.0.111"

port=8080
s.bind((host,port))
print("")
print("waiting for incoming connection....")
print("")
s.listen() #number of client pcs connected
conn, addr=s.accept()
print("")
print(addr,"--has connected to the server")
print("")

command=input(str("Command : "))
conn.send(command.encode())
print("waiting for confirmation")
print("")


data=conn.recv(1024)
if data:
    print(" Command has been executed")
    print("")
   

