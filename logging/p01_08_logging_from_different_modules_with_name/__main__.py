import sys
import logging
from functools import partial

import mod1

hprint = partial(print, "\n#")

LOWEST = 1


def main() -> None:
    hprint("Basic config (enable everything)")
    logging.addLevelName(LOWEST, "LOWEST")  # create a custom level
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        level=LOWEST
    )

    hprint("Log in main")
    logging.info("MAIN_GREETINGS")

    hprint("Use mod1.do_something()")
    mod1.do_something()

    hprint("Shutting down")
    logging.shutdown()  # flushes all loggers and cleans up


if __name__ == "__main__":
    main()
