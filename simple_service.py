import sys, os, socket
import time

addr = "127.0.0.1"
#port = 1 
port = 4444 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "Socket successfully created"

s.bind((addr, port))
print "BINDING...."
s.listen(1)
print "LISTENING on ip [%s] port [%s] fd[%s]" % (addr, port, s.fileno())

while True:

    try:

        conn,addr = s.accept()
        print "ACCEPTING.... fd[%s]" % conn.fileno()
        time.sleep(2)
        data = conn.recv(1024)
        print "Received [%s]" % data
        conn.send("STEFANO BOSS")
        #conn.close()   # works
        #s.close()      # error - bad descriptor
    except socket.error as err:
        if err.errno == 111:
            print "111"
            pass

        print "%s [%s]" % (err.strerror, err.errno)
#        s.close()
    except Exception as e:
        print e.message
        conn.close()
    finally:
        conn.close()
        time.sleep(2)