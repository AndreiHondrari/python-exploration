from mod1 import *


def main() -> None:
    # try:
    do_this()

    try:
        _do_that()
    except NameError as nerr:
        # caught because _ prefixed stuff are not imported
        print("Caught", repr(nerr))


if __name__ == '__main__':
    main()
