import time
import logging
import random

from logging import handlers
from functools import partial


hprint = partial(print, "\n#")

LOWEST = 1


def main() -> None:
    print("Set up logging")
    socket_handler = handlers.SocketHandler("127.0.0.1", 5678)

    gandalf = logging.getLogger('gandalf')
    gandalf.setLevel(1)
    gandalf.addHandler(socket_handler)
    print(gandalf)

    print("Trigger log")
    for i in range(random.randint(1, 5)):
        gandalf.info(f"MESSAGE_{i}")
        time.sleep(0.2)

    print("Cleanup ...")
    logging.shutdown()

    print("STOP")


if __name__ == "__main__":
    main()
