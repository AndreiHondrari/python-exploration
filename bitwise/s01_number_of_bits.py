#!python3
"""
The formula for finding the biggest number by the number of bits is:

x = 2 ** n - 1

where n is the number of bits and x is the largest number.

By reversing this ecuation we can find the
number of bits required for a number.

n = ceil(log(x+1, 2))
(base 2 logarithm)

"""

from math import ceil, log


xlist = [9, 15, 16, 17, 29, 31, 32, 33]

for x in xlist:
    n = ceil(log(x+1, 2))
    print(f"number of bits for {x} ({x:b}) is {n}\n")
