#!python3

import functools

from typing import Generator

hprint = functools.partial(print, "\n#")


def create_evens_producer() -> Generator[int, None, None]:
    k = 0

    while True:
        k += 1
        even = 2 * k
        yield even


class StopAccumulator(Exception):
    pass


def create_accumulator() -> Generator[int, int, None]:

    total = 0

    while True:
        try:
            x: int = yield total
        except StopAccumulator:
            yield total

        total += x


def main() -> None:

    events_producer = create_evens_producer()
    accumulator = create_accumulator()

    next(accumulator)

    for i in range(10):
        even = next(events_producer)
        accumulator.send(even)

    events_producer.close()

    final: int = accumulator.throw(StopAccumulator)
    print("final total:", final)


if __name__ == "__main__":
    main()
