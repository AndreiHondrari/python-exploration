#!python3

from dataclasses import dataclass, field

from ut import p


@dataclass
class A:
    x: int
    y: int
    z: int = field(repr=False)


p("A(10, 20, 30)")
a1 = A(10, 20, 30)
print(a1)

p("A(z=10, y=20, x=30)")
a2 = A(z=10, y=20, x=30)
print(a2)

p("A(10, y=20, z=30)")
a3 = A(10, y=20, z=30)
print(a3)
