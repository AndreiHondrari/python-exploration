from socket import *
from threading import *


CON_MESSAGE = \
"""
---------------------------------------------------------------------------------------------
##### You have connected to ___N3m3X1S__'s chat server.
##### Server holds session for several clients whith whom you can interact via text messages.
---------------------------------------------------------------------------------------------
"""

BUF_SIZE = 4096


class ConnectionHandler(Thread):

	def __init__(self, name, con):
		super(ConnectionHandler, self).__init__()
		self.name = name
		self.con = con

	def recv(self):
		return self.con.recv(BUF_SIZE)

	def run(self):
		try:
			while True:
				rcvdmsg = self.recv()
				print "[RECEIVED] '{0}' from {1}".format(rcvdmsg, self.name)

				if rcvdmsg == "--CLOSE CON--":
					self.con.close()
					print "[DISCON] {} closed connection.".format(self.name)
					break
				self.con.send("__N3M3X1S__ echoes '" + rcvdmsg + "'")
		except KeyboardInterrupt:
			pass

	def __del__(self):
		print "[DESTROY] {} destroyed !".format(self.name)


class ChatServerDefaults(object):

	DEFAULT_CON_MESSAGE = "### WELCOME TO CHAT SERVER 1.0 ###"
	DEFAULT_PORT = 5557


class ChatServer(object):

	def __init__(self, port=ChatServerDefaults.DEFAULT_PORT):
		self.s = socket()
		self.host = gethostname()
		self.port = port
		self.s.bind((self.host, self.port))

		self.connections = []

	def start(self, con_message=ChatServerDefaults.DEFAULT_CON_MESSAGE):
		self.s.listen(5)

		while True:
			try:
				con, addr = self.s.accept()
				print "[CON] {} connected to server".format(addr)
				con.send(CON_MESSAGE)

				ch = ConnectionHandler(str(addr), con)
				self.connections.append(ch)
				ch.daemon = True
				ch.start()
			except KeyboardInterrupt:
				print "[KINTRPT]"
				break

			except error, e:
				print "[ER] {}".format(e)
			except:
				print "[ER] Some kind of error occured !"

		


if __name__ == "__main__":
	print "#####################################"
	print "### STARTED SERVER OF __N3M3X1S__ ###"
	print "#####################################", "\r\n"

	server = ChatServer()
	server.start(con_message=CON_MESSAGE)