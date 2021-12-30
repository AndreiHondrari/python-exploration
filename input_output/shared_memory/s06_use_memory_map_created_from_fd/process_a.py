import time
import random
import functools

from mmap import mmap

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

    NO_OF_BYTES = 10

    try:
        while True:
            hprint("New write sequence")

            # values generation
            vals = [
                random.randint(0, 255)
                for _ in range(NO_OF_BYTES)
            ]
            print("vals :", vals)

            # write encoded values
            vals_bytes = bytearray(vals)
            print("write:", vals_bytes)

            some_mmap = mmap(some_shm._fd, 10)
            some_mmap.write(vals_bytes)
            some_mmap.seek(0)  # reset position

            time.sleep(random.random())

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
