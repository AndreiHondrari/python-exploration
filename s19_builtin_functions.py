#!/usr/bin/python3

from ut import p

p("all")

print(all([True, True, False]))
print(all([True, True, True]))

p("any")

print(any([0, 0]))
print(any([0, 1]))
print(any([1, 1]))

p("any exclusive")

def anyex(itb):
    return any(itb) and not all(itb)

print(anyex([0, 0]))
print(anyex([0, 1]))
print(anyex([1, 1]))

p("bin")
print(bin(5))

p("bytearray")
print(bytearray(100))

p("callable")

print(callable(p))
print(callable(10))

p("chr")

print(chr(113))

p("cmp")
print(cmp(10, 22))

p('dellattr')
class A:pass

a = A()

setattr(a, 'ceva', 22)
print(a.ceva)
delattr(a, 'ceva')
try:
    print(a.ceva)
except AttributeError, e:
    print(e)

p("filter")

lst = [3, 5, 2, 10, 521, 2, 45251, 21 ,24141, 2, 78556]
print(filter(lambda x: x<100, lst))

p("format")

p("frozenset")

fz = frozenset([1,1,3,3,3,5,5])
print(fz)

p("hash")
print(hash(tuple({1: 222, 2: 333})))

p("hex")
print(hex(9))

p("map")
print(map(lambda x, y, z: 0 if x is None or y is None or z is None else x+y+z,)
          [1, 2, 3], [10, 20, 30], [100, 200])

p("reduce")
print(reduce(lambda x, y: x+y, [0, 1, 2, 3, 4]))