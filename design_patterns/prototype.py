#!/usr/bin/python

import copy

class AbstractPrototype(object):

	def clone(self):
		return copy.deepcopy(self)


class A(AbstractPrototype):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y


ob1 = A(x=22, y=44)
ob2 = ob1.clone()

assert(id(ob1) != id(ob2))
print ob1.x, ob1.y
print ob2.x, ob2.y
