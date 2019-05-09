#!python

from __future__ import annotations  # -> should work only in python 3.7

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

    # -> shouldn't raise a type hint error in Python 3.7 onward
    def some(a: A) -> NoReturn:
        pass
