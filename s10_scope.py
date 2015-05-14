

def f():
	lv = 11

f()

try:
	print lv
except NameError, e:
	print "[ER] " + str(e)



print "###  this does not change the global variable"
x = 10

def f2():
	x = 22
	print x

f2()
print x

print "### set global variable"

def f3():
	global x
	x = 22

f3()
print x

print "### CLOSURES"

def f4():

	y = 33
	def f4i():
		print y

	return f4i

f4()()

print "### CLOSURE NAMESPACES"

def f5():
	f5._mvar = 33
	
	def f5i():
		f5._mvar = 77

	f5i()
	print f5._mvar

f5.z = 99
print f5.z

f5()

print "-> WITH INNER NAMESPACE"
def f6():

	class InnerNamespace(object): pass

	InnerNamespace.mvar = 44

	def f6i():
		InnerNamespace.mvar = 99

	f6i()
	print InnerNamespace.mvar

f6()


