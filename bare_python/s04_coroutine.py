#!python3

import time

from typing import Coroutine

from ut import p


def handle(n: int) -> Coroutine:

    while True:
        x = yield
        print(f"COROUTINED: {n * x}")


p("Couroutines")

p("initialize coroutine")
h1 = handle(10)
next(h1)

p("send some values")
h1.send(2)
h1.send(4)
h1.send(10)

p("close coroutine")
h1.close()

p("attempt to send a last value")
try:
    h1.send(20)
except StopIteration as e:
    print(f"raised: StopIteration {e}")

p("define a coroutine with delays")


def dosome(delay: float, name: str) -> Coroutine:
    while True:
        x = yield
        for i in range(x):  # type: ignore
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
