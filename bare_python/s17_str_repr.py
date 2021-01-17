#!python3

from ut import p


class A:

    def __str__(self) -> str:
        return "somestr"

    def __repr__(self) -> str:
        return "somerepr"


a = A()
p("simple print")
print(a)

p("repr print")
print(repr(a))
