"""
FIFO Receiver
----–--------

Only receives messages from the FIFO file.
"""
import os
import pathlib
import functools
import time

hprint = functools.partial(print, "\r#")


def main() -> None:
    print("START RECEIVER")
    fifo_path = pathlib.Path("./gandalf.fifo").absolute()

    print("make fifo file ...")
    try:
        os.mkfifo(fifo_path)
    except FileExistsError as fxerr:
        print("Caught:", repr(fxerr))
        print("FIFO file exists already. Remove it first")
        exit(1)

    print("opening fifo file ...")
    fifo_file = os.open(fifo_path, os.O_RDONLY | os.O_NONBLOCK)

    hprint("start receiving ...")
    try:
        while True:
            try:
                msg = os.read(fifo_file, 1024)
                print("RECV", msg)
            except BlockingIOError:
                print("NOTHING")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nCtrl+C detected !")

    hprint("Cleaning ...")
    os.close(fifo_file)
    os.unlink(fifo_path)
    print("STOP RECEIVER")


if __name__ == "__main__":
    main()
