import sys, os, socket
import time

addr = "127.0.0.1"
port = 1 


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error %s" %(err)

s.bind((addr, port))
print "BINDING...."
s.listen(1)
print "LISTENING on ip [%s] port [%s]" % (addr, port)
while True:
    conn,addr = s.accept()
    print "ACCEPTING...."

    data = conn.recv(1024)
    print "Received [%s]" % data
    conn.send("STEFANO BOSS")
    conn.close()
    time.sleep(2)

