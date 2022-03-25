import sys
import logging
import pprint
from functools import partial

hprint = partial(print, "\n#")

LOWEST = 1


def main() -> None:
    hprint("Basic config (enable everything)")
    logging.addLevelName(LOWEST, "LOWEST")  # create a custom level
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        level=LOWEST
    )

    hprint("Create several loggers")

    """
    Notice that we add "child" loggers in two ways here:
    - logging.getLogger('parent.child')
    - parent.getChild('child')
    """
    gandalf = logging.getLogger('gandalf')
    gandalf_kek = logging.getLogger('gandalf.kek')
    gandalf_lol = gandalf.getChild('lol')

    print("KEK_PARENT", gandalf_kek.parent)
    print("LOL_PARENT", gandalf_lol.parent)

    gandalf_kek_foo = logging.getLogger('gandalf.kek.foo')
    print('FOO_PARENT', gandalf_kek_foo.parent)

    jimmy = logging.getLogger("jimmy")
    print("JIMMY_PARENT", jimmy.parent)

    hprint("Log some stuff")
    gandalf_kek.info("lipsum")
    gandalf_kek_foo.warning("dolores")
    jimmy.fatal("consectetur")

    hprint("Display all loggers")
    root_logger = logging.getLogger()
    pprint.pprint(root_logger.manager.loggerDict)

    hprint("Shutting down")
    logging.shutdown()  # flushes all loggers and cleans up


if __name__ == "__main__":
    main()
