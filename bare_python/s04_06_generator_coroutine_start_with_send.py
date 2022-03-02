#!python3

import functools

from typing import Generator, Optional

hprint = functools.partial(print, "\n#")


def some_coroutine() -> Generator[None, Optional[int], None]:
    x: Optional[int] = yield
    if x is not None:
        print("X: ", x)


def main() -> None:
    hprint("Start coroutine with send")
    c1 = some_coroutine()

    print("START")
    c1.send(None)

    try:
        c1.send(11)
    except StopIteration:
        print("STOP")


if __name__ == "__main__":
    main()
