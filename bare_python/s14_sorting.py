#!python

from typing import List

import operator

print("### BASIC SORT")
print(sorted([3, 6, 2, 4, 2, 1]))

a = [5, 2, 4, 1]
a.sort()
print(a)

print("### sort by key")

a = [(222, 3), (333, 2), (111, 1), ]
print(sorted(a, key=lambda x: x[0]))
a.sort(key=lambda x: x[1])
print(a)

print("### sort objects by attribute")


class A:
    a = 0

    def __init__(self, a: int) -> None:
        self.a = a


lst = []


import random  # noqa
for x in range(4):
    lst.append(A(random.randint(0, 100)))

print([ob.a for ob in lst])


from operator import attrgetter  # noqa
lst.sort(key=attrgetter('a'))

print([ob.a for ob in lst])

print("### REVERSE SORT")
print(sorted([5, 3, 7, 2, 6, 1], reverse=True))

print("### SORT WITH __cmp__")


class B:

    def __init__(self, b: int) -> None:
        self.b = b or 0

    def __lt__(self, other: "B") -> int:
        print("LT", self.b, other.b)
        return -1 if self.b < other.b else 0

    # no longer available in Python 3.x
    # def __cmp__(self, other):
    #     print("COMP ", self.b, other.b)
    #     return -1 if self.b < other.b else 0


lst2: List[B] = []
for _ in range(4):
    lst2.append(B(random.randint(0, 100)))

print([x.b for x in lst2])
print([x.b for x in sorted(lst2)])
print([x.b for x in sorted(lst2, reverse=True)])
print([x.b for x in sorted(lst2, key=lambda x: x.b)])
print([x.b for x in sorted(lst2, key=operator.attrgetter('b'))])
