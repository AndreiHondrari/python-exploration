"""
In this example we obtain a custom logger
"""

import sys
import logging
from functools import partial

hprint = partial(print, "\n#")


def log_stuff(logger: logging.Logger) -> None:
    logger.debug("DEFCON 5")
    logger.info("DEFCON 4")
    logger.warning("DEFCON 3")
    logger.error("DEFCON 2")
    logger.critical("DEFCON 1")


def main() -> None:
    hprint("Basic config (enable everything)")
    logging.addLevelName(1, "LOWEST")  # create a custom level
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        level=1
    )

    hprint("Create a custom logger")
    gandalf = logging.getLogger('gandalf')
    print("LOGGER", gandalf)
    print("PARENT", gandalf.parent)
    print("PROPAGATE", gandalf.propagate)

    hprint("Log with custom logger")
    log_stuff(gandalf)

    hprint("Shutting down")
    logging.shutdown()  # flushes all loggers and cleans up


if __name__ == "__main__":
    main()
