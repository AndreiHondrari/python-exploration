"""
Equivalent:

from pack1 import mod1
"""


def main() -> None:
    mod1 = __import__('pack1.mod1', fromlist=("mod1",))
    print(mod1)
    mod1.do_this()


if __name__ == '__main__':
    main()
