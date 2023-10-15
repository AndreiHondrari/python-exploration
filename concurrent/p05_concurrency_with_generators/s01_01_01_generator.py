"""
Control steps of the execution using yield
"""

from typing import Generator


def do_bla() -> Generator[None, None, None]:
    print("111")  # section A
    yield "qqq"  # release control back to main
    print("222")  # section B
    yield "zzz"  # release control back to main
    print("333")  # section C
    # no yield means generator dies -> StopIteration

    return 777


def main() -> None:
    bla = do_bla()

    k = next(bla)  # 111 <- go to section A
    print("K1", k)

    k = next(bla)  # 222 <- go to section B
    print("K2", k)

    try:
        k = next(bla)  # 333 <- go to section C

        print("K3", k)
        """
        never reached because after 333 / Section C,
        Stopiteration is raised
        """
    except StopIteration as stop_iteration_err:
        result = stop_iteration_err.value
        print("result", result)


if __name__ == "__main__":
    main()
