
class A(object):

	#  __iter__ was checked already

	def __getitem__(self, name):
		return 2412, name

	def __setitem__(self, name, value):
		print name, value

a = A()
print a['zzz']
a['fwa'] = 42152