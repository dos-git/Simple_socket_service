import sys, os, socket, time

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

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(0)
        self.fd_nr = self.socket.fileno()       # get file descriptor number




ca = None #ConnectionActive("Conn_1", addr, port, addr, port)
while True:

    try:
        ca = ConnectionActive("Conn_1", addr, port, addr, port)
        ca.socket.connect((addr, port))
    except socket.error as err:

        print "%s [%s]" % (err.strerror, err.errno)


    try:

        print "Socket fd[%s] successfully created " % ca.fd_nr
        print "[FD:%s][IP:%s][PORT:%s] connecting" % (ca.fd_nr,addr, port)

        #ca.socket.send("DOMINO BOSS")
        time.sleep(1)
#        try:
        data = ca.socket.recv(1024)
        print "Received [%s]" % data
#        except socket.error as err_1:
#            if err_1.errno == 115:
#                continue



    except socket.error as err:

        # ERRNO 111 - connection refused - no server to realize connection
        print "%s [%s]" % (err.strerror, err.errno)

        #ca.socket.send("DOMINO BOSS")
        #print "Data send"
        #d =ca.socket.recv(1024)
        #print d
    finally:
        #ca.socket.close()
        time.sleep(2)
