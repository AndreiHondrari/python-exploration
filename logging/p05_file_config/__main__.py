import pprint
import logging
import logging.config

from functools import partial

hprint = partial(print, "\n#")

LOWEST = 1


def main() -> None:
    logging.addLevelName(LOWEST, "LOWEST")

    print("Load configuration from file ...")
    logging.config.fileConfig('logging.ini')

    hprint("Active non-root loggers")
    pprint.pprint(logging.root.manager.loggerDict)

    gandalf = logging.getLogger('gandalf')
    gandalf.info("HEY HEY")


if __name__ == "__main__":
    main()
