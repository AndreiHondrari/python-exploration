"""
By default the handlers of the root logger are not set and
the list of handlers gets populated automatically if:
- you call info, warning, etc.
- you call basicConfig

By default it is set to StreamHandler.
"""

import logging
from functools import partial

hprint = partial(print, "\n#")


def main() -> None:
    hprint("Enable everything")

    """
    Default log levels
    --–---------------
    0 = NOTSET
    10 = DEBUG
    20 = INFO
    30 = WARNING
    40 = ERROR
    50 = CRITICAL

    The logger will always log messages equal or greater than
    its log level.

    By setting it to 0 we allow all levels to pass.
    """
    logging.basicConfig(level=logging.NOTSET)

    hprint("Do some logging")
    logging.debug("DEFCON 5")
    logging.info("DEFCON 4")
    logging.warning("DEFCON 3")
    logging.error("DEFCON 2")
    logging.critical("DEFCON 1")


if __name__ == "__main__":
    main()
