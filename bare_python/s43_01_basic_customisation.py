
from ut import p


if __name__ == "__main__":
    p("__format__ customisation")

    class A:

        def __format__(self, format: str) -> str:
            return f"--> A_INSTANCE_FORMATTED with {format} <--"

    res = "{:.2f}".format(A())
    print(f"{res}")

    p("__bytes__ customisation")

    class B:

        def __bytes__(self) -> bytes:
            return b"010204015"

    b1 = bytes(B())

    print(b1)
