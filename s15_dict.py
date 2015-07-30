class A:

	a = 10
	b = 22

	def __init__(self):
		self.x = 55

	def ceva(self):
		print "CEVA A", self.a
		print "CEVA DICT", self.__dict__

a = A()

print "CLS DICT", A.__dict__
print "INST DICT", a.__dict__

a.ceva()
import ipdb; ipdb.set_trace()
print "INST prop b", a.__dict__['b']

print "VARS", vars(a)
