#!/usr/bin/python


class A(object):

	nz = 555

	def __getattr__(self, name):
		return 100, name

	def __getattribute__(self, name):
		return 222, name


a = A()
a.zat

print a.ceva
print a.nz