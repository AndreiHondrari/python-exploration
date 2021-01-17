#!python3

from ut import p
from pickle import *

class A:

    def __init__(self):
        self.a = 20
        self.b = 30

    def __repr__(self):
        return f"A(a={self.a}, b={self.b})"

p("pickle and restore an instance")
a = A()
print(f"our instance: {repr(a)}")
pa = dumps(a)
print(f"pa = dumps(a) --> {pa}")

a2 = loads(pa)
print(f"loads(pa) --> {a2}")

