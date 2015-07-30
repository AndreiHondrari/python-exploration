from ut import p

from operator import *

p("lt")
print lt(1, 2)
print lt(2, 2)
print lt(2, 1)

p("le")
print le(1, 2)
print le(2, 2)
print le(2, 1)

p("eq")
print eq(1, 2)
print eq(2, 2)
print eq(2, 1)

p("ne")
print ne(1, 2)
print ne(2, 2)
print ne(2, 1)

p("ge")
print ge(1, 2)
print ge(2, 2)
print ge(2, 1)

p("gt")
print gt(1, 2)
print gt(2, 2)
print gt(2, 1)

p("not")
print not(1)
print not(int)

p("abs")
print abs(-1000)
print abs(42141.4241)
print abs(1+1j)

p("pos")
print pos(-100)
print pos(1+4j)

p("neg")
print neg(100)
print neg(1+4j)
# print neg("fawfawf")  # won't work because it's string

p("lshift")
print lshift(2, 1)  # 010 to 100

p("rshift")
print rshift(6, 1)  # 110 to 011

p("concat")
print concat([1,2], [3, 4])

p("contains")
print contains([1,2,3], 3)
print contains([1,2,3], 4)

p("countOf")
print countOf([1,2,2,3,3,3], 2)
print countOf([1,2,2,3,3,3, 4,4,4,4,4,4,4], 4)

p("getitem")
print getitem([555,666,777,888], 2)
print getitem({'z':222, 'x':555}, 'x')

p("indexOf")
print indexOf([555,666,777,888,999], 777)
print indexOf({'z':222, 'x':555}, 'z')

p("mul")  # should repeat sequences as well
print mul(5,5)
print mul(2, [3, 4])

p("setitem")
lst = {'z':222, 'x':555}
setitem(lst, 'x', 333)
print lst

lst = {'z':222, 'x':555}
setitem(lst, 'y', 333)
print lst

p("attrgetter")
class A(object):
	z = 20

clb = attrgetter('z')
a = A()
print clb(a)

p("itemgetter")
lst = {'z':222, 'x':555, 'y':333}
clb = itemgetter('z')
print clb(lst)
clb = itemgetter(2)
print clb(lst.values())

p("methodcaller")

class A(object):
	z = 20

	def myf(self, x, **kwargs):
		print "MYF", x, kwargs

a = A()
clb = methodcaller('myf', 10, some=333)
clb(a)

p("")