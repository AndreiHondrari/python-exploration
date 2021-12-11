import pack1  # if simply importing


def main() -> None:
    try:
        # will raise error because pack1's namespace does not
        # automatically include mod1
        pack1.mod1.do_something()
    except AttributeError as aerr:
        print("Caught", repr(aerr))


if __name__ == '__main__':
    main()
