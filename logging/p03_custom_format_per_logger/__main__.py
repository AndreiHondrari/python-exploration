"""
By default all loggers have the propagate flag set to True.

The propagate essentially means that each logger will handle the message
and then pass it to the parent for further handling by it.
"""
import logging
import sys
from functools import partial

hprint = partial(print, "\n#")


def main() -> None:
    root_handler = logging.StreamHandler(sys.stdout)
    gandalf_handler = logging.StreamHandler(sys.stdout)
    kek_handler = logging.StreamHandler(sys.stdout)

    PRE_FORM = "{: >10s} --> "
    root_formatter = logging.Formatter(
        f"{PRE_FORM.format('ROOT')}:{logging.BASIC_FORMAT}"
    )
    gandalf_formatter = logging.Formatter(
        f"{PRE_FORM.format('GANDALF')}:{logging.BASIC_FORMAT}"
    )
    kek_formatter = logging.Formatter(
        f"{PRE_FORM.format('KEK')}:{logging.BASIC_FORMAT}"
    )

    root_handler.setFormatter(root_formatter)
    gandalf_handler.setFormatter(gandalf_formatter)
    kek_handler.setFormatter(kek_formatter)

    logging.basicConfig(
        handlers=[root_handler],
        level=1
    )

    hprint("Set up gandalf")
    gandalf = logging.getLogger('gandalf')
    gandalf.addHandler(gandalf_handler)

    hprint("Set up gandalf.kek")
    kek = gandalf.getChild('kek')
    kek.addHandler(kek_handler)

    hprint("Trigger fatal")
    kek.fatal("BIG_PROBLEM")


if __name__ == "__main__":
    main()
