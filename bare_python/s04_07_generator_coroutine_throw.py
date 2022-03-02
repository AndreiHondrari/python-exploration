#!python3

import functools

from typing import Generator

hprint = functools.partial(print, "\n#")


class KekException(Exception):
    pass


def some_coroutine() -> Generator[None, None, None]:
    print("some_coroutine START")

    try:
        yield
    except KekException:
        print("KEK CAUGHT !")

    print("some_coroutine END")


def main() -> None:
    hprint("Start coroutine with send")
    c1 = some_coroutine()

    hprint("Go to next yield in coroutine")
    c1.send(None)

    hprint("Throw exception")
    try:
        c1.throw(KekException)
    except StopIteration:
        print("StopIteration")


if __name__ == "__main__":
    main()
