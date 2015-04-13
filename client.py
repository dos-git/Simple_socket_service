import sys, os, socket


addr = "127.0.0.1"
port = 1 


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error %s" %(err)

s.connect((addr, port))

#data = s.recv(1024)
#print "Received [%s]" % data
s.send("DOMINO BOSS")
data = s.recv(1024)
print "Received [%s]" % data
s.close()
print data


