#!python3

import weakref

from ut import p


class A:

    def __init__(self, x):
        self._x = x

    def __repr__(self):
        return f"A(x={self._x})"


p("Explore weakref")

a = A(100)
print(f"instantiated a = {a}")

r = weakref.ref(a)
print("assigned weakref to instance r = weakref.ref(a)")

print(f"r: {r}")
print(f"r(): {r()}")

p("del a")
del a

p("Data after deletion")

p(f"attempt using a")
try:
    a
except NameError as e:
    print(f"raised: {repr(e)}")
else:
    print(f"could actually use a: {a}")

print(f"r: {r}")
print(f"r(): {r()}")
