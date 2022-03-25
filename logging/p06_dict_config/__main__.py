import pprint
import logging
import logging.config

from functools import partial

hprint = partial(print, "\n#")

LOWEST = 1


def main() -> None:
    logging.addLevelName(LOWEST, "LOWEST")

    hprint("Load configuration from dictionary ...")
    CONFIGURATION = {
        "version": 1,

        "formatters": {
            "default": {
                "format": "ext://logging.BASIC_FORMAT"
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "LOWEST",
                "stream": "ext://sys.stdout",
                "formatter": "default"
            }
        },

        "loggers": {
            "gandalf": {
                "level": "LOWEST",
                "handlers": ["console"]
            }
        }
    }
    logging.config.dictConfig(CONFIGURATION)

    hprint("Active non-root loggers")
    pprint.pprint(logging.root.manager.loggerDict)

    hprint("Log something")
    gandalf = logging.getLogger('gandalf')
    gandalf.info("HEY HEY")


if __name__ == "__main__":
    main()
