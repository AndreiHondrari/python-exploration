from typing import Protocol


class Bla(Protocol):
    def do_this(self) -> None: ...
    def do_that(self) -> None: ...


class X:
    def do_this(self) -> None:
        print("X DOES THIS")


class Y:
    def do_this(self) -> None:
        print("Y DOES THIS")

    def do_that(self) -> None:
        print("Y DOES THAT")


def f1(k: Bla) -> None:
    k.do_this()


if __name__ == '__main__':
    o1 = X()
    f1(o1)

    o2 = Y()
    f1(o2)
