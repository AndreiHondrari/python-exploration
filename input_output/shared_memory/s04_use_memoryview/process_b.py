import time
import functools

from multiprocessing import (
    resource_tracker,
    shared_memory as shmem
)


hprint = functools.partial(print, "\n#")


def main() -> None:
    print("PROCESS B - START")
    NO_OF_BYTES = 10
    MID = NO_OF_BYTES // 2

    some_shm: shmem.SharedMemory

    try:
        while True:
            hprint("New read sequence")
            try:
                some_shm = shmem.SharedMemory(name="gandalf_12345")
            except FileNotFoundError as fnf_err:
                print("Shared memory was unlinked")
                print(repr(fnf_err))
                break

            # declare memory views
            section_1 = some_shm.buf[0:MID]
            section_2 = some_shm.buf[MID:NO_OF_BYTES]

            section_1_vals_bytes = bytearray()
            section_2_vals_bytes = bytearray()

            # bytes acquisition
            for i in range(MID):
                section_1_vals_bytes.append(section_1[i])
                section_2_vals_bytes.append(section_2[i])

            print("S1 bytes:", section_1_vals_bytes)
            print("S2 bytes:", section_2_vals_bytes)

            # values decoding
            section_1_vals = list(section_1_vals_bytes)
            section_2_vals = list(section_2_vals_bytes)
            print("S1 vals :", section_1_vals)
            print("S2 vals :", section_2_vals)

            section_1.release()
            section_2.release()
            resource_tracker.unregister(some_shm._name, 'shared_memory')
            some_shm.close()

            time.sleep(0.25)

    except KeyboardInterrupt:
        print("\nCtrl+C detected !")

    print("PROCESS B - END")


if __name__ == "__main__":
    main()
