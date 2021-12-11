"""
Equivalent:

import pack
"""


def main() -> None:
    pack1 = __import__('pack1')
    pack1.mod1.do_this()
    pack1.mod2.do_that()

    try:
        pack1.mod3.do_bla()
    except AttributeError as aerr:
        print("Caught", repr(aerr))


if __name__ == '__main__':
    main()
