import sys


def main() -> None:
    sys.path.insert(0, 'somelib.zip')
    import mod1
    mod1.do_something()


if __name__ == "__main__":
    main()
