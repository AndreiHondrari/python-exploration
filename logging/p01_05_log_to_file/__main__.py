import logging
from functools import partial

hprint = partial(print, "\n#")


def log_stuff(root_logger: logging.Logger) -> None:
    root_logger.debug("DEFCON 5")
    root_logger.info("DEFCON 4")
    root_logger.warning("DEFCON 3")
    root_logger.error("DEFCON 2")
    root_logger.critical("DEFCON 1")


LOWEST = 1


def main() -> None:
    hprint("Basic config (enable everything)")
    logging.addLevelName(LOWEST, "LOWEST")
    logging.basicConfig(
        level=LOWEST,
        filename="messages.log",
        filemode="w",
    )

    root_logger = logging.getLogger()

    hprint("Do some logging")
    log_stuff(root_logger)

    hprint("Shutting down")
    logging.shutdown()  # flushes all loggers and cleans up

    hprint("Show file contents")
    with open("messages.log", "r") as log_file:
        print(log_file.read())


if __name__ == "__main__":
    main()
