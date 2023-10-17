"""
Generator - `send()` method


"""
from typing import Generator


def do_generate() -> Generator[None, None, None]:
    print("step 1")
    # ------------------
    try:
        yield
    except Exception as e:
        print("caught exception:", str(e))
    # ------------------
    print("step 2")
    # ------------------
    yield
    # ------------------
    print("step 3")


def main() -> None:
    generator: Generator[None, None, None] = do_generate()

    # step 1
    generator.send(None)

    # catch exception inside and step 2
    generator.throw(Exception("some-exception"))

    # step 3 and halt
    try:
        generator.send(None)
    except StopIteration:
        print("no more")


if __name__ == "__main__":
    main()
