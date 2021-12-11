"""
Equivalent:

from pack1 import mod1

This will import in _temp whatever there is
in pack1.__init__ as well
"""


def main() -> None:
    _temp = __import__('pack1', fromlist=("mod1",))
    print(_temp)
    mod1 = _temp.mod1

    mod1.do_this()


if __name__ == '__main__':
    main()
