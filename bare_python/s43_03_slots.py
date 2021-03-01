
import timeit
from typing import Callable, Union, Optional


class A:

    def __init__(self) -> None:
        self.x: Optional[int] = None


class B:
    __slots__ = ['x']  # makes x access faster

    def __init__(self) -> None:
        self.x: Optional[int] = None


def attr_cycle(instance: Union[A, B]) -> Callable[[], None]:
    def _attr_cycle() -> None:
        instance.x = 33
        instance.x
        del instance.x

    return _attr_cycle


if __name__ == "__main__":
    a = A()
    b = B()

    print("Running ... (wait!)")
    CYCLES = 10
    res1 = timeit.repeat(attr_cycle(a), repeat=CYCLES)
    res2 = timeit.repeat(attr_cycle(b), repeat=CYCLES)  # will be faster
    print("--- DONE\n\nResults:")

    print(min(res1))
    print(min(res2))
