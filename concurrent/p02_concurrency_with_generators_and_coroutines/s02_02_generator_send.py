"""
Generator - `send()` method


"""
from typing import Generator


def show_public_props(obj):
    for prop in dir(obj):
        if not prop.startswith('__'):
            print(prop)


def do_generate() -> Generator[None, None, None]:
    print("step 1")
    yield
    print("step 2")
    yield
    print("step 3")


def main() -> None:
    generator: Generator[None, None, None] = do_generate()

    generator.send(None)  # step 1
    generator.send(None)  # step 2


if __name__ == "__main__":
    main()
