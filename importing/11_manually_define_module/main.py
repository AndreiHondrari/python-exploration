import sys

import types


def f1() -> None:
    print("DO THIS")


def main() -> None:
    # create the module
    kek = types.ModuleType(name='lol')
    kek.do_this = f1

    # inject it
    sys.modules['kazoom'] = kek

    # import it
    import kazoom

    # use it
    print("Using kazoom ...")
    kazoom.do_this()


if __name__ == "__main__":
    main()
