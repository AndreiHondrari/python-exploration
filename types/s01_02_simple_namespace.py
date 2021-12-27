import types
import functools

hprint = functools.partial(print, "\n\b#")


def do_this() -> None:
    print("Does this")


def do_that() -> None:
    print("Does that")


def main() -> None:
    ns1 = types.SimpleNamespace()
    ns1.do_this = do_this
    ns1.do_that = do_that

    ns2 = types.SimpleNamespace()
    ns2.do_bla = do_that

    hprint("ns1.do_this")
    ns1.do_this()

    hprint("ns2.do_bla")
    ns2.do_bla()


if __name__ == '__main__':
    main()
