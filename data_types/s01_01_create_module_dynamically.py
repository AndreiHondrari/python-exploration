import types
import functools

hprint = functools.partial(print, "\n\b#")


def do_this() -> None:
    print("Does this")


def do_that() -> None:
    print("Does that")


def main() -> None:
    module1 = types.ModuleType("module1")
    module1.do_this = do_this  # type: ignore[attr-defined]
    module1.do_that = do_that  # type: ignore[attr-defined]

    module2 = types.ModuleType("module2")
    module2.do_bla = do_that  # type: ignore[attr-defined]

    hprint("module1.do_this")
    module1.do_this()

    hprint("module2.do_bla")
    module2.do_bla()


if __name__ == '__main__':
    main()
