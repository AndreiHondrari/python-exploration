import io
import random
import string
import functools


hprint = functools.partial(print, "\n#")


def make_msg(amount: int) -> str:
    return "".join(random.sample(string.ascii_letters, amount))


def main() -> None:
    text_io = io.StringIO()

    MSG = make_msg(50)

    hprint("WRITE")
    print(f"write '{MSG}' to buffer")
    text_io.write(MSG)

    hprint("initial position")
    print("position:", text_io.tell())
    print("reset to 0")
    text_io.seek(0)
    print("position:", text_io.tell())

    hprint("SUBMESSAGE")
    TEST_OFFSET = 5
    print(f"read {TEST_OFFSET} chars")
    sub_msg = text_io.read(TEST_OFFSET)
    print("submessage:", sub_msg)
    print("position:", text_io.tell())

    hprint("OVERWRITE")
    OVER = "__XXXXXX__"
    print("overwrite with:", OVER)
    text_io.write(OVER)
    print('reset position to start')
    text_io.seek(0)
    print('read everything:')
    print(text_io.read())


if __name__ == "__main__":
    main()
