
VALUES = [1, 3, 5]


def provide(target):
    target.send(None)

    for val in VALUES:
        target.send(val)

    target.close()


def add(target, term):
    target.send(None)

    while True:
        value = yield
        target.send(value + term)

    target.close()


def multiply(target, factor):
    target.send(None)

    while True:
        value = yield
        target.send(value * factor)

    target.close()


def consume():
    while True:
        value = yield
        print("value", value)


def main() -> None:
    provide(
        add(
            multiply(
                consume(),
                10
            ),
            1
        )
    )


if __name__ == "__main__":
    main()
