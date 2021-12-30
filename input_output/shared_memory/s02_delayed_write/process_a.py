import time
import random
import functools

from multiprocessing import shared_memory as shmem


hprint = functools.partial(print, "\n#")


def main() -> None:
    print("PROCESS A - START")
    some_shm = shmem.SharedMemory(
        name="gandalf_12345",
        create=True,
        size=4096
    )

    hprint("Writing values to shared memory")

    COUNT = 10

    try:
        while True:
            hprint("New write sequence")

            # values generation
            vals = [
                random.randint(0, 255)
                for _ in range(COUNT)
            ]
            print("vals :", vals)

            # values encoding
            vals_bytes = bytearray(vals)
            print("bytes:", vals_bytes)

            # write encoded values to shared memory
            for i, val_byte in enumerate(vals_bytes):
                print("write", i, val_byte)
                some_shm.buf[i] = val_byte
                time.sleep(1)  # delay write

    except KeyboardInterrupt:
        print("\nCtrl+C detected !")

    hprint("Cleaning ...")
    some_shm.close()
    try:
        some_shm.unlink()
    except FileNotFoundError as fnf_err:
        print("Was unable to unlink shared memory")
        print(repr(fnf_err))
    print("Cleaning done")

    print("PROCESS A - END")


if __name__ == "__main__":
    main()
