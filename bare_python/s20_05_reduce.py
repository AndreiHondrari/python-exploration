#!python

from functools import reduce

from ut import p

p("reduce: 2 ** 2 ** 2 -> 4 ** 2 -> 4 x 4 -> 16")
print(reduce(lambda x, y: x ** y, [2, 2, 2]))