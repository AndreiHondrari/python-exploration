"""
Control steps of the execution using yield

NOTICE YOU CAN'T GET THE RETURNED VALUE
"""

from typing import Generator


def do_bla() -> Generator[None, None, None]:
    print("111")
    yield "qqq"
    print("222")
    yield "ppp"
    print("333")


def main() -> None:
    # create coroutine object
    bla = do_bla()

    # interact with coroutine
    for x in bla:
        print("step", x)

    # NOTICE YOU CAN'T GET THE RETURNED VALUE !!!


if __name__ == "__main__":
    main()
