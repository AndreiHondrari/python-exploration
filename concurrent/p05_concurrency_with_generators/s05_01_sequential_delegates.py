"""

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
                x = next(task)
                print("step", x)
            except StopIteration as stop_iteration_err:
                print("result", stop_iteration_err.value)
                continue  # skip re-adding the task to queue

            self.tasks.append(task)


loop = EventLoop()


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


def async_main():
    p1 = do_foo()
    p2 = do_bar()

    print("\ndo_foo\n", '-' * 10, sep='')
    yield from p1  # delegate to do_foo

    print("\ndo_bar\n", '-' * 10, sep='')
    yield from p2  # delegate to do_bar

    print()


def main() -> None:
    loop.call_soon(async_main())
    loop.run()


if __name__ == "__main__":
    main()
