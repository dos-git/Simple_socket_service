import sys, os, socket, time
from pprint import pprint

addr = "127.0.0.1"
#port = 1       # ports < 4000 dedicated for a system
port = 4444

class ConnectionActive(object):

    def __init__(self, connection_name, local_ip, local_port, remote_ip, remote_port):

        self.connectio_name = connection_name
        self.local_ip_address = local_ip
        self.local_port_nr = local_port
        self.remote_ip_address = remote_ip
        self.remote_port_nr = remote_port

        self.socket = None
        self.fd_nr =  None #self.socket.fileno()       # get file descriptor number

    def Create_Socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(0)
        self.socket.settimeout(3)               # timeout for accepting connection
        self.fd_nr = self.socket.fileno()

ca = ConnectionActive("Conn_1", addr, port, addr, port)
while True:

    try:
        #ca = ConnectionActive("Conn_1", addr, port, addr, port)
        ca.Create_Socket()
        ca.socket.connect((addr, port))

    except socket.error as err:
        if err.errno == 115:
            pass
        else:
            print "[ERRNO:%03d] %s" % (err.errno, err.strerror)

    try:
#        print "Socket fd[%s] successfully created " % ca.fd_nr
#        print "[FD:%s][IP:%s][PORT:%s] connecting" % (ca.fd_nr,addr, port)

        time.sleep(0.001)       #IMPORTANT - needed small delay to realize connection
        data = ca.socket.recv(1024)

        if data != '':
            print "Received [%s]" % data

        ca.socket.send("Domi Lobek")
    except socket.error as err:
        # ERRNO 011 -   Resource temporarily unavailable (needed small
        #               timeout in order to realize connect procedure
        # ERRNO 111 -   Connection refused - no server to realize connection
        if err.errno == 111 or err.errno == 11:
            continue
        print "[ERRNO:%03d] %s" % (err.errno, err.strerror)

    finally:
        #ca.socket.close()
        time.sleep(2)
