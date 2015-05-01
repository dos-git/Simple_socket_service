import sys, os, socket, time
import Connection

addr = "127.0.0.1"
port = 4444


while True:

    ca = Connection.Connection_Active("Conn_Actv_1", addr, port, addr, port)
    print "Socket fd[%s] successfully created" %  ca.fd_nr

    rc = ca.Try_Connect()
    #rc =2
    if rc != 0:
        time.sleep(2)
        ca.socket.close()
        continue
    ca.Data_Reading()
    ca.Data_Writing()



    time.sleep(2)
