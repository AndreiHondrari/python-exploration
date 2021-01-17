#!python3

import sys
import errno

from typing import (
    NoReturn, TypeVar
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


APlaceholder = TypeVar('APlaceholder', bound="A")


# check class as a type
class A:

    # throws a type hint error because A is not yet defined
    # though this does not work until Python 3.6
    # it was established to work in 3.7 onward
    # -> should raise a type hint error in Python 3.6 and lower
    def some(a: A) -> NoReturn:
        pass

    def some2(a: "A") -> NoReturn:
        pass

    def some3(a: APlaceholder) -> NoReturn:
        pass
