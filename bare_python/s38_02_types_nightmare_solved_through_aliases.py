#!python

import sys
import errno

from typing import (
    Tuple,
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)

# nightmare type hinting
e: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]

# type hint aliases
MyIntPairAlias = Tuple[int, int]
f: Tuple[MyIntPairAlias, MyIntPairAlias, MyIntPairAlias, MyIntPairAlias]
f = 10  # -> should display type hint error
