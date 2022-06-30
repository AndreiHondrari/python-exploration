"""
By default all loggers have the propagate flag set to True.

The propagate essentially means that each logger will handle the message
and then pass it to the parent for further handling by it.
"""
import logging
import sys
import os
from functools import partial

hprint = partial(print, "\n#")


def main() -> None:

    try:
        os.unlink('root.log')
    except FileNotFoundError:
        print("root.log does not exists")

    try:
        os.unlink('gandalf.log')
    except FileNotFoundError:
        print("gandalf.log does not exists")

    try:
        os.unlink('kek.log')
    except FileNotFoundError:
        print("kek.log does not exists")

    stream_handler = logging.StreamHandler(sys.stdout)
    root_log_fh = logging.FileHandler("root.log")
    gandalf_log_fh = logging.FileHandler("gandalf.log")
    kek_log_fh = logging.FileHandler("kek.log")

    logging.basicConfig(
        handlers=[stream_handler, root_log_fh],
        level=1
    )

    hprint("Set up gandalf")
    gandalf = logging.getLogger('gandalf')
    gandalf.addHandler(gandalf_log_fh)

    hprint("Set up gandalf.kek")
    kek = gandalf.getChild('kek')
    kek.addHandler(kek_log_fh)

    hprint("Trigger fatal")
    kek.fatal("BIG_PROBLEM")


if __name__ == "__main__":
    main()
