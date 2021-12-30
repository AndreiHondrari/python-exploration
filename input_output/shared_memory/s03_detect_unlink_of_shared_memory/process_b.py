import time
import functools

from multiprocessing import (
    resource_tracker,
    shared_memory as shmem
)


hprint = functools.partial(print, "\n#")


def main() -> None:
    print("PROCESS B - START")
    some_shm: shmem.SharedMemory

    COUNT = 10

    try:
        while True:
            hprint("New read sequence")
            try:
                some_shm = shmem.SharedMemory(name="gandalf_12345")
            except FileNotFoundError as fnf_err:
                print("Shared memory was unlinked")
                print(repr(fnf_err))
                break

            vals_bytes = bytearray()

            # bytes acquisition
            for i in range(COUNT):
                vals_bytes.append(some_shm.buf[i])

            print("bytes:", vals_bytes)

            # values decoding
            vals = list(vals_bytes)
            print("vals :", vals)

            some_shm.close()

            time.sleep(0.25)

    except KeyboardInterrupt:
        print("\nCtrl+C detected !")

    # shared memory close
    print("Closing shared memory ...")
    resource_tracker.unregister(some_shm._name, 'shared_memory')

    print("PROCESS B - END")


if __name__ == "__main__":
    main()
