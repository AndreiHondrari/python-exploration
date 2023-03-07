"""
Concurrency with generators

Let's say we would like to run
111 do foo part 1
222 do bar part 1
AAA do foo part 2
BBB do bar part 2

Carefully select which task runs at which time
"""


def do_foo():
    print("111")
    yield
    print("AAA")


def do_bar():
    print("222")
    yield
    print("BBB")


def main() -> None:
    foo = do_foo()
    bar = do_bar()

    # foo part 1
    next(foo)

    # bar part 1
    next(bar)

    # foo part 2
    try:
        next(foo)
    except StopIteration:
        pass

    # bar part 2
    try:
        next(bar)
    except StopIteration:
        pass


if __name__ == "__main__":
    main()
