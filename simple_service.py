import sys, os, socket
import time
from pprint import pprint

addr = "127.0.0.1"
#port = 1 
port = 4444 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(3)     # set timeout for 3 seconds

print "Socket fd[%s] successfully created" %  s.fileno()

try:
    # IP address should be bound with port just one time
    s.bind((addr, port))
    print "Socket has been successfully bound."
except socket.error as err:
    print "Socket binding has failed - [%s][ERRNO:%s]" % (err.strerror, err.errno)

# max connection's peer that should be handled
s.listen(1)
conn = None

while True:

    try:
        print "[FD:%s][IP:%s][PORT:%s] Listening" % (s.fileno(), addr, port)
        conn, addr_2 = s.accept()
        print "[FD:%s][IP:%s][PORT:%s] Accepting connection..." % (conn.fileno(), addr_2[0], addr_2[1])

        data = conn.recv(1024)
        print "Received [%s]" % data

        conn.send("STEFANO BOSS")
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
if s:
    s.close()
