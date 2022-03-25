import logging

import pack1

LOWEST = 1


def main() -> None:
    logging.addLevelName(LOWEST, "LOWEST")
    logging.basicConfig(level=1)

    pack1.mod1.do_this()
    pack1.mod2.do_that()


if __name__ == "__main__":
    main()
