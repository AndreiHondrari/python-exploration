#!python3

"""
Execution:
- coroutine is created

- main calls send(None) on coroutine,
  execution is passed to the start of the coroutine;
  notice the None ->
    the coroutine would not accept anything else, because there was
    no yield waiting to receive a value from outside

- coroutine executes until the first yield, execution is passed back to main,
  to where it was left

- main calls send(value) on coroutine
- yield receives the value sent by main and passes it to the left hand operand

Coroutine will continue to ingest values via send until it is closed.
"""

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
