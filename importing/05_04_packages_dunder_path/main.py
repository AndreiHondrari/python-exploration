import pack1.mod1

from pack2 import mod2


def main() -> None:
    pack1.mod1.do_something()

    mod2.do_that()


if __name__ == '__main__':
    main()
