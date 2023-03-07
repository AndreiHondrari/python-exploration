"""
Control steps of the execution using yield
"""


def do_bla():
    print("111")
    yield
    print("222")
    yield
    print("333")


def main() -> None:
    bla = do_bla()

    next(bla)  # 111
    next(bla)  # 222

    try:
        next(bla)
    except StopIteration:
        pass


if __name__ == "__main__":
    main()
