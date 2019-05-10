#!python

from typing import Any, Tuple


class A:

    def __getitem__(self, name: str) -> Tuple[int, str]:
        return 2412, name

    def __setitem__(self, name: str, value: Any) -> None:
        print(name, value)


a = A()
print(a['zzz'])
a['fwa'] = 42152
