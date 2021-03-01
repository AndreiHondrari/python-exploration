

from ut import p

from typing import Optional, Any


class SomeDescriptor:

    def __init__(
        self,
        initial_value: Optional[Any] = None
    ) -> None:
        self._initial_value = initial_value

    def __set_name__(self, obj: Any, name: str) -> None:
        print(f"__set_name__ call: {obj}, {name}")

    def __get__(
        self,
        obj: Any,
        obj_type: Optional[Any] = None
    ) -> Any:
        print(f"__get__ call: {obj}: {obj_type}")
        return self._initial_value

    def __set__(self, obj: Any, value: Any) -> None:
        print(f"__set__ call: {obj}, {value}")
        self._initial_value = value

    def __delete__(self, obj: Any) -> None:
        print(f"__del__ called: {obj}")
        self._initial_value = None


class A:
    x = SomeDescriptor(55)


if __name__ == "__main__":

    a1 = A()

    p("a1.x")
    a1.x

    p("a1.x = 333")
    a1.x = 333

    p("del a1.x")
    del a1.x
