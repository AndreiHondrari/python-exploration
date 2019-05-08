#!python

import sys
import errno

from typing import (
    TypeVar, Any, Generic, NoReturn,
    List, Tuple, Dict, Iterable, Sequence,
    Callable,
    MutableSet, FrozenSet
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)

# simple type hinting
a: int = 10
b: int = "not integer obviously"  # -> should display type hint error
c: list = [1, "not int", 3]  # will suggest that you need to use a List
d: List[int] = [1, 2, 3]
d1: Dict[int, str]
d1 = {10: "abc"}
d1 = {22: 222}  # -> should display type hint error

# nightmare type hinting
e: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]

# type hint aliases
MyIntPairAlias = Tuple[int, int]
f: Tuple[MyIntPairAlias, MyIntPairAlias, MyIntPairAlias, MyIntPairAlias]
f = 10  # -> should display type hint error


# simple function type hinting
def some(x: int) -> None:
    pass


some(10)
some(10.241421)  # -> should display type hint error


# Explicit no return function type hinting
def willnotreturn() -> None:
    return 100  # -> should display type hint error


def willnotreturn2() -> NoReturn:
    return 100  # -> should display type hint error


# typevar type hinting
T = TypeVar('T', int, float)


def generic(x: T) -> None:
    pass


generic(10)
generic(22.3)
generic(True)
generic([])  # -> should display type hint error
generic("bla")  # -> should display type hint error
generic(lambda x: x)
generic(some)


# Any type hint
def anything(x: Any) -> Any:  # can't use Any directly
    return 22


T1 = TypeVar('T1')


def anything2(x: T1) -> Generic[T1]:
    return 22


anything(10)


# Callable type hint
def callback() -> NoReturn:
    pass


def call_the_callback(cbk: Callable[[], NoReturn]) -> NoReturn:
    cbk()


call_the_callback(callback)
call_the_callback(anything)


# Callable with variable argument list
def call_the_callback2(cbk: Callable[..., NoReturn]) -> NoReturn:
    cbk()


call_the_callback2(callback)

call_the_callback2(anything)
# -> Returns a type hint error because
# it expects the callback to have some arguments

call_the_callback2(anything2)


# Check iterables type hinting
def process_iterable(it: Iterable[int]) -> NoReturn:
    pass


process_iterable([10, 20])
process_iterable(["bla", 22.344])  # -> should display type hint error
process_iterable("not iterable obviously")  # -> should display type hint error


# check sequences type hinting
def process_sequence(seq: Sequence[Any]) -> NoReturn:
    pass


process_sequence((10, 20, ))
process_sequence([10, 20, ])  # oddly enough it does not work with lists
process_sequence("abcdefgh")


# check mutable sets and frozen sets
ms1: MutableSet[int] = set()
ms2: MutableSet[int] = frozenset()

fs1: FrozenSet[int] = frozenset()
fs2: FrozenSet[int] = set()
