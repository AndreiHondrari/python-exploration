"""
Concurrency with generators

Let's say we would like to run
111 do foo part 1
AAA do bar part 1
222 do foo part 2
BBB do bar part 2
333 do foo part 3
CCC do bar part 3

Run parts of the tasks until they are done.
"""

from collections import deque


def do_foo():
    print("111")
    yield 444
    print("222")
    yield 555
    print("333")

    return 7777


def do_bar():
    print("AAA")
    yield "DDD"
    print("BBB")
    yield "EEE"
    print("CCC")

    return 9999


def main() -> None:
    tasks = deque()

    # declare some tasks
    foo = do_foo()
    bar = do_bar()

    tasks.append(foo)
    tasks.append(bar)

    # run the tasks in a round-robin fashion
    while tasks:
        task = tasks.popleft()

        try:
            x = next(task)
            print("step", x)
        except StopIteration as stop_iteration_err:
            print("result", stop_iteration_err.value)
            continue  # skip re-adding the task to queue

        tasks.append(task)

    print("\nDONE")


if __name__ == "__main__":
    main()
