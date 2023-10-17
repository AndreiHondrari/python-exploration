
from typing import Generator


def do_generate() -> Generator[None, None, None]:
    print("before")
    yield
    print("after")


def main() -> None:
    generator: Generator[None, None, None] = do_generate()

    gen_props = [
        prop
        for prop in dir(generator)
        if not prop.startswith('__')
    ]

    for x in gen_props:
        print(x)


if __name__ == "__main__":
    main()
