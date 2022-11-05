import logging
from pathlib import Path
from logging import handlers
from functools import partial
from typing import Final

hprint = partial(print, "\n#")


def main() -> None:
    LOG_FILENAME = "something.log"
    LOG_FILE_EXISTS: Final[bool] = Path(LOG_FILENAME).absolute().exists()

    root_handler = handlers.RotatingFileHandler(
        LOG_FILENAME,
        backupCount=5
    )

    logging.basicConfig(
        handlers=[root_handler],
        level=1
    )

    if LOG_FILE_EXISTS:
        root_handler.doRollover()

    hprint("Trigger log")
    for i in range(10):
        logging.error(f"\t COUNT_{i} something something \t done.")


if __name__ == "__main__":
    main()
