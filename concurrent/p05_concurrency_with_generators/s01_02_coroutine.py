"""
Control steps of the execution using yield
"""

from typing import Generator


def do_bla() -> Generator[None, None, None]:
    print("111")
    yield
    print("222")
    yield
    print("333")


def main() -> None:
    bla = do_bla()

    bla.send(None)  # 111
    bla.send(None)  # 222

    try:
        bla.send(None)  # 333
    except StopIteration:
        pass


if __name__ == "__main__":
    main()
