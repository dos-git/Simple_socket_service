import sys, os, socket
import time
from pprint import pprint
import Connection

addr = "127.0.0.1"
port = 4444 

cp = Connection.Connection_Passive("Conn_Pass_1", addr, port)
cp.Listening()
conn = None

while True:

    rc = cp.Accept_Connection()
    print "RC [%s]" % rc
    if rc == 7:
        continue

    #cp.Data_Reading()
    #cp.Data_Writing()



