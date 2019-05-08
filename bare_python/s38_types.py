#!python

import sys
import errno

from typing import (
    TypeVar, Any, Generic,
    List, Tuple, Dict, Iterable, Sequence,
    Callable,
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

# nightmare type hinting
e: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]

# type hint aliases
MyIntPairAlias = Tuple[int, int]
f: Tuple[MyIntPairAlias, MyIntPairAlias, MyIntPairAlias, MyIntPairAlias]
f = 10  # -> should display type hint error


# simple function type hinting
def some(x: int) -> None:
    '''cartof'''
    pass


some(10)
some(10.241421)  # -> should display type hint error

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
