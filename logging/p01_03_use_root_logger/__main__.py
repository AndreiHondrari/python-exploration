"""
We can interact directly with the root logger by acquiring it with:

root_logger = logging.getLogger()
"""

import logging
import types
from typing import List
from functools import partial

hprint = partial(print, "\n#")


def display_logger_props(
    properties: List[str],
    root_logger: logging.Logger
) -> None:

    for p in properties:
        member = getattr(root_logger, p)

        # for methods
        if isinstance(member, types.MethodType):
            print(f"root_logger.{p}() -> ", end="")
            result = member()
            print(result)

        # for attributes
        else:
            print(f"root_logger.{p} =", member)


HANDLERS_PROPS = [
    "hasHandlers", "handlers",
]

PROPS = [
    "disabled", "filters",  "getEffectiveLevel",
]


def main() -> None:
    hprint("Get the logger")
    root_logger = logging.getLogger()
    print(root_logger)

    hprint("Display some root logger properties")
    display_logger_props(PROPS, root_logger)
    display_logger_props(HANDLERS_PROPS, root_logger)

    hprint("Do basic config")
    logging.basicConfig()

    hprint("Display root logger properties (again)")
    display_logger_props(HANDLERS_PROPS, root_logger)

    hprint("Do some logging")
    root_logger.debug("DEFCON 5")
    root_logger.info("DEFCON 4")
    root_logger.warning("DEFCON 3")
    root_logger.error("DEFCON 2")
    root_logger.critical("DEFCON 1")


if __name__ == "__main__":
    main()
