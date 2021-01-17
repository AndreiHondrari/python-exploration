#!python3

from typing import Tuple

from ut import p


def f() -> Tuple[int, int, int]:
    return 1, 2, 3


p("unpack to tuple of vars")
(a, b, c) = f()

print(a)
print(b)
print(c)

p("listify/tuplify")
print(tuple(f()))
print(list(f()))

p("unpack directly to vars -> theoretically still a tuple")
x, y, z = f()
print(x)
print(y)
print(y)

try:
    x, y = f()  # type: ignore
except ValueError:
    print("ValueError raised")
