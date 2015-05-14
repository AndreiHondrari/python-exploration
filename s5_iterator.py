
class MyIter(object):

	x = 10
	limit = 0

	def __init__(self, limit):
		self.limit = limit

	def next(self):
		tx = self.x

		if tx > self.limit:
			raise StopIteration()

		self.x *= 2

		return tx

	def __iter__(self):  # -> makes this class an iterator class
		return self

m = MyIter(200)
a = iter(m)

print type(a)

print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()  # -> raises StopIteration