
import sys
import logging


def main() -> None:
    this_fmt = logging.Formatter(f"_AAA_:{logging.BASIC_FORMAT}")
    that_fmt = logging.Formatter(f"_ZZZ_:{logging.BASIC_FORMAT}")

    lol_filter = logging.Filter("kek.lol")
    foo_filter = logging.Filter("kek.foo")

    handler_1 = logging.StreamHandler(sys.stdout)
    handler_1.setFormatter(this_fmt)
    handler_1.addFilter(lol_filter)  # make sure that it receives only kek.foo

    handler_2 = logging.StreamHandler(sys.stdout)
    handler_2.setFormatter(that_fmt)
    handler_2.addFilter(foo_filter)  # make sure that it receives only kek.lol

    root_logger = logging.getLogger()
    root_logger.setLevel(9999)

    kek = logging.getLogger("kek")
    kek.setLevel(1)

    kek.addHandler(handler_1)
    kek.addHandler(handler_2)

    lol = kek.getChild("lol")
    heh = lol.getChild("heh")

    foo = kek.getChild("foo")
    bar = foo.getChild("bar")

    heh.info("HEY")
    bar.info("UHM")


if __name__ == "__main__":
    main()
