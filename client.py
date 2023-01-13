import socket
import sys
import os
import time

s=socket.socket()
# host="127.0.0.1"
host="192.168.0.102"

port=8080
s.connect((host,port))

print("Established connection to: ",host,":",port)
command=s.recv(1024)
command=command.decode()

if command =="shutdown":
    print("Shutdown command")
    s.send("Command is received".encode())
    os.system("Shtdwn.bat")

elif command=="logout":
    print("Log out command")
    s.send("command is received".encode())
    os.system("logoff.bat")

elif command =="restart":
    print("Restart command")
    s.send("restart command is received".encode())
    os.system("reboot.bat")

elif command=="sleep":
    print("Sleep command")
    s.send("Hibernate command is received".encode())
    os.system("hibernate.bat")

elif command =="formatdisk":
    print("format disk command")
    s.send("formating drive command is received".encode())
    os.system("delete.bat")

elif command=="disconnect":

    s.send("Disconnecting command recieved".encode())
    print("disconnected from server command")
    quit()