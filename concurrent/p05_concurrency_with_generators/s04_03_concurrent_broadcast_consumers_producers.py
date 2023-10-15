
VALUES = [1, 3, 5]


def broadcast(targets):
    # start targets
    for target in targets:
        target.send(None)

    # broadcast to targets
    for val in VALUES:
        for target in targets:
            target.send(val)

    target.close()


def consume(message):
    while True:
        value = yield
        print(f"[{message}] value", value)


def main() -> None:
    broadcast([consume('aaa'), consume('bbb')])


if __name__ == "__main__":
    main()
