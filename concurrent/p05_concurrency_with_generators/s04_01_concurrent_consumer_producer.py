"""

"""


def produce():
    for i in range(3):
        print(f"foo {i}")
        yield i


def consume(other):
    yield from other


def main() -> None:
    foo = produce()
    bar = consume(foo)

    # execution loop
    while True:
        try:
            bar.send(None)
        except StopIteration:
            print("DONE")
            break


if __name__ == "__main__":
    main()
