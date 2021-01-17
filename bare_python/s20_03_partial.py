#!python3

from functools import partial


def some(msg: str) -> None:
    print(f"{msg}")


predef_some = partial(some, "predefined some !!!")
other_some = partial(some, "other some !!!")

some("initial some")
predef_some()
other_some()
