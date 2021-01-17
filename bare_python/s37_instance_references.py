#!python3

from ut import p


class A:

    def __init__(self, x):
        self._x = x

    def __repr__(self):
        return f"A(x={self._x})"

a1 = A(100)
p(f"instantiated a1 = {a1}")

a2 = a1
p(f"referenced instance a2 = a1")

p("del a1")
del a1


p(f"attempt using a1")
try:
    a1
except NameError as e:
    print(f"raised: {repr(e)}")
else:
    print(f"could actually use a1: {a1}")

p(f"attempt using a2")
try:
    a2
except NameError as e:
    print(f"raised: {repr(e)}")
else:
    print(f"could actually use a2: {a2}")
