#!python

from typing import Any

from contextlib import AbstractContextManager as ACM

from ut import p


class A(ACM):

    def __init__(self) -> None:
        self.x = 10

    def __exit__(self, *args: Any) -> None:
        # needs to be implemented because it's abstract in ACM
        pass


p("ACM normal")
with A() as a:
    print(vars(a))
