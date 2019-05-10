#!python

from typing import Iterator


def myf(chestii: Iterator[int]) -> None:
    for x in chestii:
        print(x)


myf(z for z in [1, 2, 3])
