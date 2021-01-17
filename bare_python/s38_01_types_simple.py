#!python3

import sys
import errno

from typing import (
    List, Tuple, Dict
)

from ut import p

# this script is only for type hint checking purposes
# type hinting is not enforced during runtime.
# The purpose is to check how mypy handles type hinting
p("! NOT MEANT TO BE EXECUTED -> EXITING !")
sys.exit(errno.EINTR)

# simple type hinting
a: int = 10
b: int = "not integer obviously"  # -> should display type hint error

c: list = [1, "not int", 3]  # will suggest that you need to use a List
d: List[int] = [1, 2, 3]

d1: Dict[int, str]
d1 = {10: "abc"}
d1 = {22: 222}  # -> should display type hint error

t1: Tuple[int] = (10,)
t1 = ('bla',)  # -> should display type hint error
t1 = (10, 20,)  # -> should display type hint error


b1: int = True  # -> bool is a subset of int
b2: bool = 10  # -> should display type hint error
