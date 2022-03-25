import logging
from logging import handlers
from functools import partial

hprint = partial(print, "\n#")


def main() -> None:
    root_handler = handlers.RotatingFileHandler(
        'something.log',
        maxBytes=1,
        backupCount=5
    )

    logging.basicConfig(
        handlers=[root_handler],
        level=1
    )

    hprint("Trigger log")
    for i in range(10):
        logging.error(f"\t COUNT_{i} something something \t done.")


if __name__ == "__main__":
    main()
