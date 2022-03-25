import time
import logging
from logging import handlers
from functools import partial

hprint = partial(print, "\n#")


def main() -> None:
    root_handler = handlers.TimedRotatingFileHandler(
        'something.log',
        backupCount=2,
        when='S'
    )

    logging.basicConfig(
        handlers=[root_handler],
        level=1
    )

    hprint("Trigger log")
    for i in range(13):
        msg = f"\t COUNT_{i} something something \t done."
        print(msg)
        logging.error(msg)
        time.sleep(0.25)


if __name__ == "__main__":
    main()
