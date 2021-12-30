"""
FIFO Sender
-----------

Only opens the FIFO file and writes into it.
"""
import os
import random
import pathlib
import functools
import time


hprint = functools.partial(print, "\r#")


def main() -> None:
    print("START SENDER")
    fifo_path = pathlib.Path("./gandalf.fifo").absolute()

    try:
        fifo_file = os.open(fifo_path, os.O_WRONLY)
        try:
            while True:
                msg = str(random.randint(1000, 10_000))
                print("SEND", msg)
                os.write(fifo_file, msg.encode())
                os.fsync(fifo_file)
                time.sleep(random.random())
        except KeyboardInterrupt:
            print("\nCtrl+C detected !")

        os.close(fifo_file)

    except FileNotFoundError as fnferr:
        print("FIFO is missing:", repr(fnferr))

    print("STOP SENDER")


if __name__ == "__main__":
    main()
