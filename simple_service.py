import sys, os, socket
import time
from pprint import pprint

addr = "127.0.0.1"
#port = 1 
port = 4444 

class ConnectionPassive(object):

    def __init__(self, connection_name, local_ip, local_port):
        self.connectio_name = connection_name
        self.local_ip_address = local_ip
        self.local_port_nr = local_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(0)
        self.socket.settimeout(3)               # timeout for accepting connection
        self.fd_nr = self.socket.fileno()       # get file descriptor number

    def Bind(self, addr, port):

        try:
            # IP address should be bound with port just one time
            self.socket.bind((addr, port))
            print "Socket has been successfully bound."
            self.socket.listen(1)
        except socket.error as err:
            print "Socket binding has failed - [%s][ERRNO:%s]" % (err.strerror, err.errno)

    def Accept_Connection(self):

        conn, addr_conn = self.socket.accept()
        return conn, addr_conn
# max connection's peer that should be handled

conn = None

counter = 0
data_to_send = "BACK SEND"

cp = ConnectionPassive("Conn_Passive",addr, port)
cp.Bind(addr, port)
while True:

    try:
        print "[FD:%s][IP:%s][PORT:%s] Listening" % (cp.fd_nr, addr, port)
        conn, addr_2 = cp.Accept_Connection()
        print "[FD:%s][IP:%s][PORT:%s] Accepting connection..." % (conn.fileno(), addr_2[0], addr_2[1])


        #conn.send("STEFANO BOSS")

        if counter < 5:

            conn.send(data_to_send)
        counter += 1


        data = conn.recv(1024)
        print "Received [%s]" % data


        conn.close()   # works
        #s.close()      # error - bad descriptor

    except socket.error as err:

        # timeout - cannot accept and realize connection
        if err.message and err.message == "timed out":
            continue

        print "Exception - [%s][%s][%s]" % (err.strerror, err.errno, err.message)

    except Exception as e:
        print e.message
        if conn:
            conn.close()
    finally:
        if conn:
            conn.close()
            time.sleep(2)

# terminate socket
if cp.socket:
    cp.socket.close()
