
def fdec(f):

	def wrapper():
		print "PRE F"
		f()
		print "POST F"

	return wrapper


print "### direct call of the decorator"
def myf():
	print "MYF"


fdec(myf)()



print "### syntactic sweet decorator call"
@fdec
def myf2():
	print "MYF 2"

myf2()


print "### decorator with extra parameters"

def fdec2(param1, param2):
	
	def innerDecorator(f):

		def wrapper(fparam1, fparam2):
			print "PRE F", param1, param2
			f(fparam1, fparam2)
			print "POST F", param1, param2

		return wrapper

	return innerDecorator


@fdec2("PARAM1", "PARAM2")
def myf3(a, b):
	print "MYF 3", a, b

myf3("FPARAM1", "FPARAM2")


print "### callable instance decorator"

class mycdec(object):

	def __init__(self, f):
		self.f = f

	def __call__(self):
		print "PRE C DEC"
		self.f()
		print "POST C DEC"

@mycdec
def myf4():
	print "MYF4"

myf4()

print "### callable instance decorator with arguments"

class mycdec(object):

	def __init__(self, param1, param2):
		pass

	def __call__(self, f):
		def fwrapper(fparam1):
			print "PRE C DEC"
			f(fparam1)
			print "POST C DEC"

		return fwrapper


@mycdec("PARAM1", "PARAM2")
def myf4(fparam):
	print "MYF4", fparam

myf4("FPARAM1")