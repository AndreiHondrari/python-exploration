#!python3

from typing import Any


class A:
    z = 555

    def __setattr__(self, name: str, value: Any) -> None:
        print(name, value)
        self.__dict__['z'] = value


a = A()
a.z = 10

print(a.z)
