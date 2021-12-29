"""
FIFO Receiver
----–--------

Only receives messages from the FIFO file.
"""
import os
import pathlib
import functools

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
    with open(fifo_path, "r") as fifo_file:

        hprint("start receiving ...")
        try:
            while True:
                msg = fifo_file.readline()
                print("RECV", msg.strip())
        except KeyboardInterrupt:
            print("\nCtrl+C detected !")

    hprint("Cleaning ...")
    os.unlink(fifo_path)
    print("STOP RECEIVER")


if __name__ == "__main__":
    main()
