#!python3

from ctypes import CDLL


someext = CDLL("./someext.so")
someext.something()
x: int = someext.give()
print(f"someext.give(): {x}")
