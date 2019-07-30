#!python

from typing import Tuple, Any
from ut import p

p("A")


class A:

    x = 555

    def __getattr__(self, name: str) -> Tuple[int, str]:
        return 100, name

    def __getattribute__(self, name: str) -> Tuple[int, str]:
        return 222, name


a = A()
# __getattribute__ is always called no matter what
print(a.x)
print(a.y)

p("B")


class B:

    x = 555

    def __getattr__(self, name: str) -> Tuple[int, str]:
        return 100, name

    def __getattribute__(self, name: str) -> Tuple[int, str]:
        raise AttributeError()
        return 333


b = B()
# __getattr__ is always called because __getattribute__ is called first and
# raises an AttributeError
print(b.x)
print(b.y)

p("C")


class C:

    x = 555

    def __getattr__(self, name: str) -> Tuple[int, str]:
        return 100, name


c = C()
print(c.x)  # -> it is found so the actual value is returned
print(c.y)  # -> it is not found so __getattr__ is called

p("D")


class D:

    x = 555

    def __getattr__(self, name: str) -> Any:
        return self.z
        # --> causes this __getattr__ to be called again because
        # z does not exist in this instance
        # hence infinite recursion occurs


d = D()
print(d.x)
p("d.y hidden --> raises exception")
# print(d.y)  # -> this triggers the initial __getattr__ call

p("E")


class E:
    x = 555

    def __getattr__(self, name: str) -> Any:
        return self.__dict__[name]


e = E()
print(e.x)  # --> gets the value from self.__dict__
try:
    print(e.y)
except Exception as e:
    print("e.y raises {}".format(str(e.__repr__())))

p("F")


class F:

    def __init__(self):
        self.x = 10

    def __getattr__(self, name: str) -> Any:
        return f"{name} not found"


f = F()
print(f.x)
print(f.y)
