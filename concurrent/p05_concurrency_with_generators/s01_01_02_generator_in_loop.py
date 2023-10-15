"""
Control steps of the execution using yield

NOTICE YOU CAN'T GET THE RETURNED VALUE
"""

from typing import Generator


def do_bla() -> Generator[None, None, int]:
    print("111")  # section A
    yield "qqq"  # release control back to main
    print("222")  # section B
    yield "ppp"  # release control back to main
    print("333")  # section C
    # no yield means generator dies -> StopIteration

    return 777


def main() -> None:
    bla = do_bla()

    for x in bla:
        print("step", x)

    # NOTICE YOU CAN'T GET THE RETURNED VALUE !!!


if __name__ == "__main__":
    main()
