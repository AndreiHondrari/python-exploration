"""
Calling info, warning, etc. from the logging module will pass the call
to the root logger (existing and created by default by the module).
"""

import logging
from functools import partial

hprint = partial(print, "\n#")


def main() -> None:
    hprint("Do some logging")
    logging.debug("DEFCON 5")
    logging.info("DEFCON 4")
    logging.warning("DEFCON 3")
    logging.error("DEFCON 2")
    logging.critical("DEFCON 1")


if __name__ == "__main__":
    main()
