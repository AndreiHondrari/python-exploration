"""

"""

from collections import deque
from typing import Generator


def produce(source: str, multiplier: int):
    for i in range(2):
        x = multiplier * (i + 1)
        print(f"[{source}] {x}")
        yield x


def consume(
    other: Generator[int, None, None],
    tag: str
):
    print(f"[{tag}] PRE")
    x = yield from other
    print(f"[{tag}] POST {x}")


def main() -> None:
    source_1 = produce("source-1", 11)
    source_2 = produce("source-2", 1111)

    tasks = deque()

    tasks.append(consume(source_1, "task-1"))
    tasks.append(consume(source_2, "task-2"))

    # event loop
    while tasks:
        task = tasks.popleft()
        try:
            x = next(task)
            print(f"{x}")
        except StopIteration:
            continue

        tasks.append(task)


if __name__ == "__main__":
    main()
