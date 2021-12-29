"""
FIFO Receiver
----–--------

Only receives messages from the FIFO file.
"""
import os
import pathlib
import functools

from typing import Optional, TextIO


hprint = functools.partial(print, "\n#")


def main() -> None:
    print("START RECEIVER")
    fifo_path = pathlib.Path("./gandalf.fifo").absolute()

    # FIFO creation
    hprint("try make fifo file ...")
    try:
        os.mkfifo(fifo_path)
        print("FIFO file created")
    except FileExistsError:
        print("FIFO file detected. Another receiver is running !")
        exit(1)

    # FIFO handling
    fifo_file: Optional[TextIO] = None

    try:

        # FIFO cycle
        hprint("start cycling FIFO file ...")
        while True:
            hprint("opening FIFO file ...")
            fifo_file = open(fifo_path, "r")

            hprint("start receiving ...")
            while True:
                msg = fifo_file.readline()
                if len(msg) == 0:
                    print("EOF detected. cycle ...")
                    break

                print("RECV", msg.strip())

            print("Close FIFO file ...")
            fifo_file.close()

    except KeyboardInterrupt:
        print("\nCtrl+C detected !")
        if fifo_file is not None:
            print("Close FIFO file ...")
            fifo_file.close()

    except FileNotFoundError as fnferr:
        print("Abnormal: FIFO is missing:", repr(fnferr))

    hprint("Cleaning ...")
    os.unlink(fifo_path)

    print("STOP RECEIVER")


if __name__ == "__main__":
    main()
