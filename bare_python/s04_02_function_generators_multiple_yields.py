#!python3

from typing import Iterator


def gen(n: int) -> Iterator[int]:
    yield 1
    yield 2
    yield 3
    yield 4


# return 0 -> raises SyntaxError
# (can't have return and yield in a generator function)
a = gen(4)
print(a)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))  # -> yields StopIteration
