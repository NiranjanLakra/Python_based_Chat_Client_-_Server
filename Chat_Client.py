import socket
import threading
import sys
import os
import signal
import time

server_ip=sys.argv[1]
server_port=int(sys.argv[2])
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((server_ip,server_port))
banner="Welcome to Conventional_Breakers Network"
print
print banner
print
name=raw_input("enter your name :")
client_socket.send(name)
def acceptor(client_socket):
        while True:
                try:
                        data1=client_socket.recv(1024)
                        print data1
                except:
                        pass
        print"Acceptor thread ending\n"

acceptor_thread=threading.Thread(target=acceptor,args=(client_socket,))
acceptor_thread.start() 
while True:
	data=raw_input("<<:")
	if data=='exit':
		client_socket.send('exit')
		client_socket.close()
		break
	else:
		client_socket.send(data)
print" main thread aboout to exit \n"
os.kill(os.getppid(),signal.SIGHUP)
