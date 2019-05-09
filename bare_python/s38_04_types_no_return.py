#!python

import sys
import errno

from typing import (
    NoReturn,
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# Explicit no return function type hinting
def willnotreturn() -> None:
    return 100  # -> should display type hint error


def willnotreturn2() -> NoReturn:
    return 100  # -> should display type hint error
