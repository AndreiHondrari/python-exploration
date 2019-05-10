#!python

import itertools
from typing import Iterable, Any, List

from ut import p


def take(n: int, iterable: Iterable[Any]) -> List[Iterable[Any]]:
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))


p("TAKE 1")
print(take(5, (x for x in [1, 2, 3])))

p("SLICED")
sliced = itertools.islice((x for x in [1, 2, 3]), 5)
print(type(sliced))
print(list(sliced))
