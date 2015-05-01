import sys, os, socket, time

from Connection import Connection_Active
from pprint import pprint

addr = "127.0.0.1"
#port = 1       # ports < 4000 dedicated for a system
port = 4444



ca = Connection_Active("Conn_1", addr, port, addr, port)
while True:

    ca.Create_Socket()
    rc = ca.Try_Connect()
    if rc != 0:
        time.sleep(2)
        continue

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

        # timeout (no errno, only message)
        if type(err) is  socket.timeout:
            continue

        print "[ERRNO:%03d][%s] Exception caught." % (err.errno, err.strerror)

    finally:
        #ca.socket.close()
        time.sleep(2)
