#!python3

from typing import Type, Any
from ut import p


class A:

    def __enter__(self) -> None:
        print("ENTER")

    # (exc_type, exc_value, traceback)
    def __exit__(
        self,
        exc_type: Type[Exception],
        exc_value: str,
        traceback: Any
    ) -> None:
        print("EXIT exc_type", exc_type)
        print("EXIT exc_value", exc_value)
        print("EXIT traceback", traceback)


p("normal context")
with A() as a:
    print("IN WITH")

p("context with exception raised")
try:
    with A() as e:
        raise Exception("some exception")
except Exception:
    print("Exception detected!")

p("return something random")


class B:

    def __enter__(self) -> int:
        return 123

    def __exit__(self, *args: Any) -> None:
        pass


with B() as x:
    print(x)
