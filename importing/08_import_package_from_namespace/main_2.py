"""
Re-iterated example of 02_01_subdir_import
"""

import mynamespace


def main() -> None:
    try:
        mynamespace.pack1.mod1.do_something()
    except AttributeError:
        print("Caught AttributeError")


if __name__ == "__main__":
    main()
