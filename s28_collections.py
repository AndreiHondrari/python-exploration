#!/usr/bin/python3

from ut import *
from collections import *

p("namedtuple")
CartesianCoordinate = namedtuple("CartesianCoordinate", ['x', 'y', 'z'])
print(CartesianCoordinate(10, 20, 30))

p("regular dict -> not ordered")
d = {}
d['b'] = 10
d['a'] = 22
d[33] = 22

for k,v in d.items():
    print(k, v)


p("OrderedDict")
od = OrderedDict()
od['b'] = 10
od['a'] = 22
od[33] = 22

for k,v in od.items():
    print(k, v)

p("operations")
print([1,2,3] + [2,3])
print([x for x in [214,412,412, 1,2,3,4,5,6] if x not in [1,2]])