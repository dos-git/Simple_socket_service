import os, sys
import socket
import threading
import errno

NOERROR = 0

ERR_NO_CONNECTION = 11

ERR_FAILURE_CONNECT = 80
ERR_FAILURE_BIND = 90
ERR_NOITEM = 99

class Connection(object):

    STATE_CONNECTED = 0     # connected with a peer
    STATE_DISCONNECTED = 1  # disconnected with a peer
    STATE_CONNECTING = 2    # pending connection
    STATE_LISTENING = 3     # connected, ready to acquire data
    STATE_OBSOLETE = 4      # state when we do not need it any more

    def __init__(self, connection_name, local_ip, local_port):

        self.state = Connection.STATE_DISCONNECTED
        self.connection_name = connection_name
        self.local_ip_address = local_ip
        self.local_port_nr = local_port
        self.socket = None
        self.fd_nr = 0                 # get file descriptor number
        self.lock = threading.RLock()

    def Create_Socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(0)
        self.socket.settimeout(3)               # timeout for accepting connection
        self.fd_nr = self.socket.fileno()


class Connection_Passive(Connection):

    def __init__(self, connection_name, ip_address, port_nr):

        super(Connection_Passive, self).__init__(connection_name, ip_address, port_nr)

    def Create_Socket(self):
        super(Connection_Passive, self).Create_Socket()

    def Bind(self, addr, port):

        try:
            # IP address should be bound with port just one time
            self.socket.bind((addr, port))
            self.socket.listen(1)
            self.state = Connection.STATE_LISTENING
            print "Socket is listening..."
        except socket.error as err:
            self.state = Connection.STATE_DISCONNECTED
            print "[ERRNO:%03d][%s] Socket binding has failed." % (err.errno, err.strerror)

    def Accept_Connection(self):

        conn, addr_conn = self.socket.accept()
        return conn, addr_conn



class Connection_Active(Connection):

    def __init__(self, connection_name, local_ip_address, local_port_nr, remote_ip_address, remote_port_nr):

        super(Connection_Active, self).__init__(connection_name, local_ip_address, local_port_nr)
        self.remote_ip_address = remote_ip_address
        self.remote_port_nr = remote_port_nr


    def Try_Connect(self):

        try:
            self.socket.connect((self.remote_ip_address, self.remote_port_nr))
            self.state = Connection.STATE_CONNECTED
            print "Connection[%s] has been created" % self.connection_name
            return NOERROR

        except socket.error as err:

            if err.errno == 111:
                print "[ERRNO:%03d][%s] Connection could not be realized" % (err.errno, err.strerror)
            else:

                print "[ERRNO:%03d][%s] Connection could not be realized" % (err.errno, err.strerror)

            return ERR_FAILURE_CONNECT

