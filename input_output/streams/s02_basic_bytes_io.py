import io
import random
import functools


hprint = functools.partial(print, "\n#")


def make_bytes(amount: int) -> bytes:
    return bytes([random.randint(0, 255) for _ in range(amount)])


def main() -> None:
    bytes_io = io.BytesIO()

    hprint("WRITE")
    BYTES = make_bytes(20)

    print("write")
    print(BYTES)
    print(list(BYTES))

    bytes_io.write(BYTES)

    hprint("POSITION")
    print("position:", bytes_io.tell())
    print("reset position")
    bytes_io.seek(0)

    hprint("SUB SEQUENCE")
    TEST_OFFSET = 5

    print(f"read {TEST_OFFSET} bytes")
    sub_seq = bytes_io.read(TEST_OFFSET)

    print("subsequence")
    print(sub_seq)
    print(list(sub_seq))

    print("position:", bytes_io.tell())

    hprint("OVERWRITE")
    OVER = bytes([0, 0, 0, 255, 255, 255, 0, 0, 0])

    print("overwrite")
    print(OVER)
    print(list(OVER))
    bytes_io.write(OVER)
    print("position:", bytes_io.tell())

    print("reset position to start")
    bytes_io.seek(0)
    print("read all")
    current_all = bytes_io.read()
    print(current_all)
    print(list(current_all))


if __name__ == "__main__":
    main()
