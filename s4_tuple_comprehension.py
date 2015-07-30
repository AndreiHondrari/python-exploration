#!/usr/bin/python

a = (x for x in xrange(3))

print a.next()
print a.next()
print a.next()
print a.next() #  -> raises StopIteration