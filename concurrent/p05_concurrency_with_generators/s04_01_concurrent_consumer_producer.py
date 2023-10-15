

VALUES = [1, 3, 5]


def producer(target):
    target.send(None)

    for val in VALUES:
        target.send(val)

    target.close()


def consumer():
    while True:
        value = yield
        print("value", value)


def main() -> None:
    c1 = consumer()
    producer(c1)


if __name__ == "__main__":
    main()
