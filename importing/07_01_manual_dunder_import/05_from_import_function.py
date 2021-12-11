"""
Equivalent:

from pack1.mod1 import do_this
"""


def main() -> None:
    _temp_mod = __import__('pack1.mod1', fromlist=("mod1",))
    do_this = _temp_mod.do_this

    do_this()


if __name__ == '__main__':
    main()
