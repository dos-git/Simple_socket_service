import sys, os, socket
import time

from Connection import Connection_Passive
from pprint import pprint

addr = "127.0.0.1"
#port = 1 
port = 4444 


conn = None

counter = 0
data_to_send = "BACK SEND"

cp = Connection_Passive("Conn_Passive",addr, port)
cp.Create_Socket()
cp.Bind(addr, port)
while True:

    try:
        print "[FD:%s][IP:%s][PORT:%s] Listening" % (cp.fd_nr, addr, port)
        conn, addr_2 = cp.Accept_Connection()
        print "[FD:%s][IP:%s][PORT:%s] Accepting connection..." % (conn.fileno(), addr_2[0], addr_2[1])

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

    finally:
        if conn:
            conn.close()
            time.sleep(2)

# terminate socket
if cp.socket:
    cp.socket.close()
