import sys, os, socket, time


addr = "127.0.0.1"
#port = 1 
port = 4444


while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:

        print "Socket fd[%s] successfully created " % s.fileno()
        print "[FD:%s][IP:%s][PORT:%s] connecting" % (s.fileno(),addr, port)
        s.connect((addr, port))

        s.send("DOMINO BOSS")
        data = s.recv(1024)
        print "Received [%s]" % data

    except socket.error as err:

        # ERRNO 111 - connection refused - no server to realize connection
        print "%s [%s]" % (err.strerror, err.errno)

    finally:
        s.close()
        time.sleep(2)
