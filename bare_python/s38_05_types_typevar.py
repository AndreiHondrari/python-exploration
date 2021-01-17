#!python3

import sys
import errno

from typing import (
    TypeVar, NoReturn,
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# typevar type hinting
T = TypeVar('T', int, float)


def generic(x: T) -> None:
    pass


def some() -> NoReturn:
    pass


generic(10)
generic(22.3)
generic(True)  # -> bool is a subset of int
generic([])  # -> should display type hint error
generic("bla")  # -> should display type hint error
generic(lambda x: x)  # -> should display type hint error
generic(some)  # -> should display type hint error
