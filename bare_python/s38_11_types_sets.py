#!python3

import sys
import errno

from typing import (
    MutableSet, FrozenSet
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)


# check mutable sets and frozen sets
ms1: MutableSet[int] = set()
ms2: MutableSet[int] = frozenset()  # -> should display type hint error

fs1: FrozenSet[int] = frozenset()
fs2: FrozenSet[int] = set()  # -> should display type hint error
