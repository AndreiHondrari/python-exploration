class A(object):
	
	def __enter__(self):
		print "ENTER"

	def __exit__(self, type, value, traceback):
		print "EXIT", type, value, traceback


with A() as a:
	print "IN WITH"