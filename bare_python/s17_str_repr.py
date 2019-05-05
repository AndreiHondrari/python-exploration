#!python

from ut import p


class A:

    def __str__(self):
        return "somestr"

    def __repr__(self):
        return "somerepr"

a = A()
p("simple print")
print(a)

p("repr print")
print(repr(a))