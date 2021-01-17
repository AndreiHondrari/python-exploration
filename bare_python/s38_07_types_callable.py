#!python3

import sys
import errno

from typing import (
    NoReturn, Callable,
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# Callable type hint
def callback() -> NoReturn:
    pass


def call_the_callback(cbk: Callable[[], NoReturn]) -> NoReturn:
    cbk()


def anything(x: int) -> NoReturn:
    pass


call_the_callback(callback)
call_the_callback(anything)  # -> should display type hint error
