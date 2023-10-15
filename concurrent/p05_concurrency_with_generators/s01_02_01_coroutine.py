"""
Control steps of the execution using yield
"""

from typing import Generator


def do_bla() -> Generator[None, None, None]:
    print("111")
    yield "qqq"
    print("222")
    yield "ppp"
    print("333")

    return 777


def main() -> None:
    # create coroutine object
    bla = do_bla()

    # interact with coroutine
    k = bla.send(None)  # 111
    print("K1", k)

    k = bla.send(None)  # 222
    print("K2", k)

    try:
        k = bla.send(None)  # 333

        print("K2", k)
        """
        never reached because after 333 / Section C,
        Stopiteration is raised
        """
    except StopIteration as stop_iteration_err:
        result = stop_iteration_err.value
        print("result", result)


if __name__ == "__main__":
    main()
