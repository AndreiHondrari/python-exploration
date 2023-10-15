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


def async_main():
    # create coroutine object
    bla = do_bla()

    result = yield from bla
    print("result", result)


def main() -> None:
    async_main_instance = async_main()
    [() for _ in async_main_instance]  # a ultra simple event loop
    print("async main finished")


if __name__ == "__main__":
    main()
