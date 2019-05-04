#!/usr/bin/python3

import itertools
from ut import p

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

p("TAKE 1")
print(take(5, (x for x in [1, 2, 3])))

p("SLICED")
sliced = itertools.islice((x for x in [1, 2, 3]), 5)
print(type(sliced))
print(list(sliced))