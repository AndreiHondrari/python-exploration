#!python

import sys
import errno

from typing import (
    NoReturn, Iterable,
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# Check iterables type hinting
def process_iterable(it: Iterable[int]) -> NoReturn:
    pass


process_iterable([10, 20])
process_iterable(["bla", 22.344])  # -> should display type hint error
process_iterable("not iterable obviously")  # -> should display type hint error
