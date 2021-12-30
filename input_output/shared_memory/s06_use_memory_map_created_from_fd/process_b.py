import time
import functools

from mmap import mmap

from multiprocessing import (
    resource_tracker,
    shared_memory as shmem
)


hprint = functools.partial(print, "\n#")


def main() -> None:
    print("PROCESS B - START")
    some_shm: shmem.SharedMemory

    NO_OF_BYTES = 10

    try:
        while True:
            hprint("New read sequence")
            try:
                some_shm = shmem.SharedMemory(name="gandalf_12345")
            except FileNotFoundError as fnf_err:
                print("Shared memory was unlinked")
                print(repr(fnf_err))
                break

            # bytes acquisition
            some_mmap = mmap(some_shm._fd, 10)
            vals_bytes = some_mmap.read(NO_OF_BYTES)

            print("bytes:", vals_bytes)

            # values decoding
            vals = list(vals_bytes)
            print("vals :", vals)

            resource_tracker.unregister(some_shm._name, 'shared_memory')
            some_shm.close()

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nCtrl+C detected !")

    print("PROCESS B - END")


if __name__ == "__main__":
    main()
