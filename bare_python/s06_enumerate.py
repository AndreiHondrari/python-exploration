#!python3

from copy import deepcopy

enum1 = enumerate(["a", "b", "c"])
enum2 = deepcopy(enum1)

print(enum1)

print([x for x in enum1])
print({x[0]: x[1] for x in enum2})
