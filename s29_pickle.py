#!/usr/bin/python3

from ut import p
from pickle import *

class A:

    def __init__(self):
        self.a = 20
        self.b = 30

    # def __str__(self):
    #     return "zafuk"

p("DUMPS")
a = A()
pa = dumps(a)
a2 = loads(pa)

print(a2.a)
print(a2.b)

