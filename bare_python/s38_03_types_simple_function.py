#!python3

import sys
import errno

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# simple function type hinting
def some(x: int) -> None:
    pass


some(10)
some(10.241421)  # -> should display type hint error
