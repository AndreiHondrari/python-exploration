import sys
import logging
from functools import partial

hprint = partial(print, "\n#")

LOWEST = 1


def main() -> None:
    hprint("Basic config (enable everything)")
    logging.addLevelName(LOWEST, "LOWEST")  # create a custom level
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        level=LOWEST,
        format="%(asctime)s %(message)s"
    )

    hprint("Log some stuff")
    logging.info("Hello")

    hprint("Shutting down")
    logging.shutdown()  # flushes all loggers and cleans up


if __name__ == "__main__":
    main()
