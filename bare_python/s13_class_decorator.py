#!python3

from typing import Any, Callable


def myClassDecorator(OriginalClass: Any) -> Any:

    class WrapperClass(OriginalClass):  # type: ignore

        def __init__(self) -> None:
            print("PRE INIT")
            OriginalClass.__init__(self)
            print("POST INIT")

        def ceva(self) -> None:
            print("PRE ceva")
            OriginalClass.ceva(self)
            print("POST ceva")

    return WrapperClass


@myClassDecorator
class MyClass:

    def __init__(self) -> None:
        print("MCLASS INIT")

    def ceva(self) -> None:
        print("MCLASS CEVA")


a = MyClass()

a.ceva()

print("### method decorator")


def mdec(m: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper(self: Any) -> None:
        print("PRE M")
        m(self)
        print("POST M")

    return wrapper


class A:

    @mdec
    def am(self) -> None:
        print("AM")


oba = A()
oba.am()
