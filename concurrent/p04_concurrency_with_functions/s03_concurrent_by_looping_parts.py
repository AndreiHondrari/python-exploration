"""
Concurrent function parts in a loop

Let's say we would like to run
111 do foo part 1
222 do bar part 1
AAA do foo part 2
BBB do bar part 2

Concurrency of functionality parts from a loop.
"""

from collections import deque


# do foo
def do_foo_part_1():
    print("111")


def do_foo_part_2():
    print("AAA")


# do bar
def do_bar_part_1():
    print("222")


def do_bar_part_2():
    print("BBB")


def main() -> None:
    tasks = deque()

    tasks.append(do_foo_part_1)
    tasks.append(do_bar_part_1)
    tasks.append(do_foo_part_2)
    tasks.append(do_bar_part_2)

    # events loop
    for task in tasks:
        task()


if __name__ == "__main__":
    main()
