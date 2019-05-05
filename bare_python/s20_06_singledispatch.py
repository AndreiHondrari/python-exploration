#!python

from functools import singledispatch

@singledispatch
def some(x):
    print(f"INTEGER: {x}")


@some.register(float)
def _some(x):
    print(f"FLOAT: {x}")


@some.register(complex)
def _some(x):
    print(f"COMPLEX: {x}")


some(10)
some(20.99)
some(1+2j)
