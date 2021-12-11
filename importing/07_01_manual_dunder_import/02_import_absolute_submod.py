"""
This will import whatever there is in pack1.__init__ as well
"""


def main() -> None:
    pack1 = __import__('pack1.mod1')
    print(pack1)
    pack1.mod1.do_this()
    pack1.mod2.do_that()


if __name__ == '__main__':
    main()
