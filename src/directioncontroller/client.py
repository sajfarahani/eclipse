import sys
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8192
BUFFER_SIZE = 1024
param = []
i=0

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP,TCP_PORT))
#s.listen(1)

#print 'Listening for client...'

#conn, addr = s.accept()
#print 'Connection address:', addr
def client_socket():
    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP,TCP_PORT))
        s.listen(1)
        while 1:
            print 'Listening for client...'
            conn, addr = s.accept()
            print 'Connection address:', addr
            data = conn.recv(BUFFER_SIZE)
            if data == ";" :
                conn.close()
                print "Received all the data"
                i=0
                for x in param:
                    print x
                #break
            elif data:
                print "received data: ", data
                param.insert(i,data)
                i+=1
                #print "End of transmission"
        s.close()