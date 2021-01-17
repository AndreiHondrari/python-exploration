#!python3

import sys
import errno

from typing import (
    NoReturn, Any, Sequence,
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# check sequences type hinting
def process_sequence(seq: Sequence[Any]) -> NoReturn:
    pass


process_sequence((10, 20, ))
process_sequence([10, 20, ])  # oddly enough it does not work with lists
process_sequence("abcdefgh")
