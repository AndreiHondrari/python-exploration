#!/usr/bin/python3

import copy

from ut import p


class A:

    def __init__(self, x):
        p("A.__init__ called")
        self.x = x


p("OBJECT DIRECT ASSIGNMENT")
ob1 = A(10)
ob2 = ob1

p("OB1 and OB2 ID's")
print(id(ob1), id(ob2))
assert(id(ob1) == id(ob2))

p("INITIAL OB*.X")
print(ob1.x, ob2.x)

p("ALTERED OB*.X")
ob1.x = 33
print(ob1.x, ob2.x)

p("OB's SHALLOW COPY")
ob3 = copy.copy(ob1)
print(id(ob1), id(ob3))

p("SHALLOW COPIES INITIAL OB*.X")
print(ob1.x, ob3.x)

p("SHALLOW COPIES ALTERED OB*.X")
ob1.x = 44
print(ob1.x, ob3.x)