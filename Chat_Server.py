banner="+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
banner1="|S|T|R|U|G|G|L|E|R|-|N|O|O|B|-|C|Y|B|E|-|S|E|C|.|"
banner2="+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
print banner.center(145,' '),
print banner1.center(144,' '),
print banner2.center(144,' ')
import socket								# imported socket library for Server-Client communication
import sys								# sys module for getting arguments from command line
import threading							# module for Multi-Threading
import time

server_ip=sys.argv[1]                  # determining server ip from 1st command line argument
server_port=int(sys.argv[2])	       # determining server port from 2nd command line argument
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)          # creation of IPv4 TCP socket 
server_socket.bind((server_ip,server_port))				# binding server ip and port
server_socket.listen(100)		# defining the no of connections the server can handle
client_list=[]				# creation of global list to keep track of client sockets
client_name=[]
# data_broadcaster Function to brodcast data to all other clients 
def data_broadcaster(data,client_socket,name):
    global client_list
    for client in client_list:
        if not client==client_socket:
            client.send(name +" << "+ data)

# data_acceptor function for continously accepting data from clients 
def data_acceptor(client_socket):
    global client_list
    global client_name
    name=client_socket.recv(1024)
    client_name.insert(0,name)
    print name+' connected'
    while True:
        try:
            data=client_socket.recv(1024)
	    #print client_list
	    if data=="exit":
		data_broadcaster("left",client_socket,name)
		time.sleep(0.5)
		client_list.remove(client_socket)
		client_name.remove(name)
		break
	    else:
		print"-----------------"
	    	print name +">>"+ data 
            	data_broadcaster(data,client_socket,name)
            	data_list.insert(0,data)
        except:
            pass
    print name+" left"
# loop to continously accept onnections
while True:
    try:
        client_socket,addr=server_socket.accept()
        #print"%s connected from port %d",(addr[0],addr[1])
        client_list.append(client_socket)
        #print client_list
        data_acceptor_thread=threading.Thread(target=data_acceptor,args=(client_socket,))
        data_acceptor_thread.start()
    except Exception as e :
        print str(e) + "HAPPENED"
