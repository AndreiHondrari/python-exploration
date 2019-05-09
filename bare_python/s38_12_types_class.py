#!python

import sys
import errno

from typing import (
    NoReturn
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# check class as a type
class A:
    pass


def something(a: A) -> NoReturn:
    pass


something(A())
something(10)  # -> should display type hint error
