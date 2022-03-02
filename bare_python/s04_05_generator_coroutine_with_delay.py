#!python3

import time

from typing import Generator

from ut import p


def dosome(delay: float, name: str) -> Generator[None, int, None]:
    while True:
        x: int = yield
        for i in range(x):
            time.sleep(delay)
            print(f"[{name}]: {i}")


d1 = dosome(0.2, "DELAYED COROUTINE 1")
d2 = dosome(0.5, "DELAYED COROUTINE 2")

next(d1)
next(d2)

p("send some values to the delayed coroutines")
d1.send(4)
d2.send(5)

p("DONE")
