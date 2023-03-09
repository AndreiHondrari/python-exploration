#!python3

"""
Execution:
- coroutine is created
- main calls next on coroutine, execution is passed to the coroutine
- executing it up to first yield, execution is passed back to main,
  to where it was left
- main calls send on coroutine
- yield receives the value sent by main and passes it to the left hand operand

Coroutine will continue to ingest values via send until it is closed.
"""

import time

from typing import Generator

from ut import p


def handle(n: int) -> Generator[None, int, None]:

    while True:
        x: int = yield
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
