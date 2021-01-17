#!python3

from ut import p


class A:

    a = 10

    def __call__(self, x: int) -> int:
        return x + self.a


a_callable = A()

p("callable resulting from instantiating")
print(a_callable(3))
