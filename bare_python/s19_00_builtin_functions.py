#!python

from typing import Iterable

from ut import p

p("abs")
print(abs(-1))

p("all")

print(all([True, True, False]))
print(all([True, True, True]))

p("any")

print(any([0, 0]))
print(any([0, 1]))
print(any([1, 1]))

p("any exclusive")


def anyex(itb: Iterable) -> bool:
    return any(itb) and not all(itb)


print(anyex([0, 0]))
print(anyex([0, 1]))
print(anyex([1, 1]))

p("bin")
print(bin(5))

p("bytearray")
print(bytearray(10))
print(bytearray([0x01, 0x01, 0x0f]))
print(bytearray("a".encode("utf-8")))
print(bytearray("b", "utf-8"))
ba1 = bytearray([0x01, 0x01, 0x0f])
print(ba1[2])
ba1[0] = 0xfe
print(ba1[0])

p("bytes (immutable version of bytearray)")
# bytes is an immutable version of bytearray
print(bytes(10))
try:
    bytes(10)[0] = 0xfe  # type: ignore
except Exception as e:
    print(f"raises {repr(e)}")

p("callable")

print(callable(p))
print(callable(10))

p("chr")

print(chr(113))

p('dellattr')


class A:
    pass


a = A()

setattr(a, 'ceva', 22)
print(a.ceva)  # type: ignore
delattr(a, 'ceva')
try:
    print(a.ceva)  # type: ignore
except AttributeError as e:
    print(e)

p("divmod")
res, rem = divmod(5, 3)
print(f"result {res} and remainder {rem} of divmod(5, 3)")

p("filter")
lst = [3, 5, 2, 10, 521, 2, 45251, 21, 24141, 2, 78556]
print(filter(lambda x: x < 100, lst))

p("format")
print(format(9, 'b'))
print(format(999, '>10d'))

p("frozenset")
fz = frozenset([1, 1, 3, 3, 3, 5, 5])
print(fz)

p("hash")
print(hash(tuple({1: 222, 2: 333})))

p("hex")
print(hex(9))

p("map")
print(
    map(  # type: ignore
        lambda x, y, z: 0  # type: ignore
        if x is None or y is None or z is None else x+y+z,
        ([1, 2, 3], [10, 20, 30], [100, 200],)
    )
)

p("vars")


class B:
    def __init__(self) -> None:
        self.x = 10


print(vars(B()))


OBJ = type('X', (object,), {})
print(vars(OBJ()))

p("type")
print(type('X', (object,), {}))
