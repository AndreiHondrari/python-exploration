"""
In this example we attempt at disabling logging under (including)
a certain log level and then re-enabling it.

Disabling -> logging.disable(target log level)
Re-enabling -> logging.disable(logging.NOTSET)
"""

import sys
import logging
from functools import partial

hprint = partial(print, "\n#")


def log_stuff(root_logger: logging.Logger) -> None:
    root_logger.debug("DEFCON 5")
    root_logger.info("DEFCON 4")
    root_logger.warning("DEFCON 3")
    root_logger.error("DEFCON 2")
    root_logger.critical("DEFCON 1")


def main() -> None:
    hprint("Basic config (enable everything)")
    """
    We are setting the StreamHandler to sys.stdout
    because by default it is created for sys.stderr.

    We want sys.stdout because sys.stderr is not buffered and
    all the log messages are flushed after the execution of the script.
    (or otherwise said the order of logging does not matter for stderr)
    """
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.NOTSET
    )

    hprint("Disable below level ERRORS")
    logging.disable(logging.WARNING)

    hprint("Get root logger")
    root_logger = logging.getLogger()

    hprint("Do some logging")
    log_stuff(root_logger)

    hprint("Re-enable")
    logging.disable(logging.NOTSET)

    hprint("Do some logging")
    log_stuff(root_logger)

    hprint("Shutting down")
    logging.shutdown()  # flushes all loggers and cleans up


if __name__ == "__main__":
    main()
