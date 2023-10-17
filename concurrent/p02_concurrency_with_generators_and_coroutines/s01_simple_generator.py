
from typing import Generator


def do_generate() -> Generator[None, None, None]:
    print("before")
    yield
    print("after")


def main() -> None:
    generator: Generator[None, None, None] = do_generate()
    next(generator)


if __name__ == "__main__":
    main()
