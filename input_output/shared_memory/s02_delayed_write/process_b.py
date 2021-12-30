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
        # shared memory opening
        hprint("Opening shared memory ...")
        some_shm = shmem.SharedMemory(name="gandalf_12345")
        print("Shared memory opened")

        try:
            while True:
                hprint("New read sequence")
                vals_bytes = bytearray()

                # bytes acquisition
                for i in range(COUNT):
                    vals_bytes.append(some_shm.buf[i])

                print("bytes:", vals_bytes)

                # values decoding
                vals = list(vals_bytes)
                print("vals :", vals)

                time.sleep(0.25)

        except KeyboardInterrupt:
            print("\nCtrl+C detected !")

        # shared memory close
        print("Closing shared memory ...")
        resource_tracker.unregister(some_shm._name, 'shared_memory')
        some_shm.close()

    except FileNotFoundError as fnf_err:
        print("Could not find shared memory")
        print(repr(fnf_err))

    print("PROCESS B - END")


if __name__ == "__main__":
    main()
