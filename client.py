import sys, os, socket, time


addr = "127.0.0.1"
#port = 1 
port = 4444


while True:

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print "Socket fd[%s] successfully created " % s.fileno()

        print "CONNECTING to ip [%s] port [%s] fd[%s]" % (addr, port, s.fileno())
        s.connect((addr, port))
        #data = s.recv(1024)
        #print "Received [%s]" % data
        s.send("DOMINO BOSS")
        data = s.recv(1024)
        print "Received [%s]" % data
        #s.close()
        print data
    except socket.error as err:
        print "%s [%s]" % (err.strerror, err.errno)

    finally:
        s.close()
        time.sleep(2)
