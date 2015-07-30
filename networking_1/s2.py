from socket import *

print "#####################################"
print "### STARTED CLIENT OF __N3M3X1S__ ###"
print "#####################################", "\r\n"

skt = socket()
host = gethostname()
PORT = 5557

try:
	skt.connect((host, PORT))

	BUF_SIZE = 4096
	CLOSE_CON = "--CLOSE CON--"

	con_message = skt.recv(BUF_SIZE)
	print con_message

	while True:
		try:
			user_input = raw_input("TYPE: ")
			if user_input == "S_EXIT":
				skt.send(CLOSE_CON)
				break

			skt.send(user_input)
			rcvdmsg = skt.recv(BUF_SIZE)
			print "SERVER: " + rcvdmsg
		except KeyboardInterrupt:
			skt.send(CLOSE_CON)
			break	

	skt.close()
except error, e:
	print "Error: {}".format(e)