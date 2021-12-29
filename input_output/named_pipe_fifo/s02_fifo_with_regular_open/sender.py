"""
FIFO Sender
-----------

Only opens the FIFO file and writes into it.
"""

import random
import pathlib
import functools
import time


hprint = functools.partial(print, "\r#")


def main() -> None:
    print("START SENDER")
    fifo_path = pathlib.Path("./gandalf.fifo").absolute()

    try:
        hprint("opening fifo file ...")
        with open(fifo_path, "w") as fifo_file:
            hprint("start sending ...")
            try:
                while True:
                    msg = str(random.randint(1000, 10_000))
                    print("SEND", msg)
                    fifo_file.write(msg + "\n")
                    fifo_file.flush()
                    time.sleep(random.random())
            except KeyboardInterrupt:
                print("\nCtrl+C detected !")

    except FileNotFoundError as fnferr:
        print("FIFO is missing:", repr(fnferr))

    print("STOP SENDER")


if __name__ == "__main__":
    main()
