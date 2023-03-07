"""
Concurrency with generators

Let's say we would like to run
111 do foo part 1
222 do bar part 1
AAA do foo part 2
BBB do bar part 2

Run parts of the tasks until they are done.
"""

from collections import deque


class EventLoop:

    def __init__(self):
        self.tasks = deque()

    def call_soon(self, task):
        self.tasks.append(task)

    def run(self):
        # run the tasks in a round-robin fashion
        while self.tasks:
            task = self.tasks.popleft()

            try:
                next(task)
            except StopIteration:
                continue  # skip re-adding the task to queue

            self.tasks.append(task)


loop = EventLoop()


def do_foo():
    print("111")
    yield
    print("AAA")


def do_bar():
    print("222")
    yield
    print("BBB")


def main() -> None:
    # declare some tasks
    foo = do_foo()
    bar = do_bar()

    loop.call_soon(foo)
    loop.call_soon(bar)

    loop.run()

    print("\nDONE")


if __name__ == "__main__":
    main()
