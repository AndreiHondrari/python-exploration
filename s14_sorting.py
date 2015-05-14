
print "### BASIC SORT"
print sorted([3,6,2,4,2,1])

a = [5,2,4,1]
a.sort()
print a

print "### sort by key"

a = [(222, 3), (333, 2), (111, 1),]
print sorted(a, key=lambda x: x[0])
a.sort(key=lambda x: x[1])
print a

print "### sort objects by attribute"

class A(object):

	a = 0
	def __init__(self, a):
		self.a = a

lst = []
import random
for x in xrange(4):
	lst.append(A(random.randint(0, 100)))

print [ob.a for ob in lst]

from operator import attrgetter
lst.sort(key=attrgetter('a'))

print [ob.a for ob in lst]

print "### REVERSE SORT"
print sorted([5,3,7,2,6,1], reverse=True)

print "### SORT WITH __cmp__"

class B(object):

	b = 0
	def __init__(self, b):
		self.b = b

	def __cmp__(self, other):
		print "COMP ", self.b, other.b
		return -1 if self.b < other.b else 0

lst = []
for x in xrange(4):
	lst.append(B(random.randint(0, 100)))

print [x.b for x in lst]
print [x.b for x in sorted(lst)]

