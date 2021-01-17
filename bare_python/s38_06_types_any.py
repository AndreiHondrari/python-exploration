#!python3

import sys
import errno

from typing import (
    Any,
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)

# TODO: FIX!


# Any type hint
def anything(x: Any) -> Any:
    return 22


anything(10)
