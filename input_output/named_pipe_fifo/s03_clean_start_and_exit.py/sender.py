"""
FIFO Sender
-----------

Only opens the FIFO file and writes into it.
"""

import random
import pathlib
import functools
import time

from typing import Optional, TextIO


hprint = functools.partial(print, "\n#")


def close_fifo(fifo_file: TextIO) -> None:
    try:
        print("Close FIFO file ...")
        fifo_file.close()
    except BrokenPipeError:
        print("BrokenPipe -> nothing to close !")


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"[{UID}] START SENDER")
    fifo_path = pathlib.Path("./gandalf.fifo").absolute()

    # FIFO handling
    fifo_file: Optional[TextIO] = None

    try:
        if not fifo_path.exists():
            raise FileNotFoundError(fifo_path)

        hprint("opening FIFO file ...")
        fifo_file = open(fifo_path, "w")

        try:
            hprint("start receiving ...")
            while True:
                msg = str(random.randint(1000, 10_000))
                msg = f"[{UID}] {msg}"
                print("SEND", msg)
                fifo_file.write(f"{msg}\n")
                fifo_file.flush()
                time.sleep(random.random())
        except BrokenPipeError:
            print("Other party closed FIFO")

        close_fifo(fifo_file)

    except KeyboardInterrupt:
        print("\nCtrl+C detected !")
        if fifo_file is not None:
            close_fifo(fifo_file)

    except FileNotFoundError as fnferr:
        hprint("FIFO is missing:")
        print(repr(fnferr))
        print("You might want to start the receiver first !")

    print("STOP SENDER")


if __name__ == "__main__":
    main()
