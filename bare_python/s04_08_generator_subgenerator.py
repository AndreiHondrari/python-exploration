#!python3

import functools

from typing import Generator, Union

hprint = functools.partial(print, "\n#")

tbprint = functools.partial(print, sep='\t')


def subgenerator1():
    print("SUBGEN 1 START")

    for i in range(3):
        val = f"{11 * (i+1)}"
        tbprint("sgen1", "pre", val)
        yield val
        tbprint("sgen1", "post", val)

    print("SUBGEN 1 STOP")


def subgenerator2():
    print("SUBGEN 2 START")

    for i in range(3):
        val = 'A' * (i + 1)
        tbprint("sgen2", "pre", val)
        yield val
        tbprint("sgen2", "post", val)

    print("SUBGEN 2 STOP")


def main_generator() -> Generator[Union[int, str], None, None]:
    hprint("main gen start")

    print(" ")
    tbprint("gen", "A", "\n")

    # delegate subgenerator with loop
    for x in subgenerator1():
        yield x

    print(" ")
    tbprint("gen", "B", "\n")

    # delete subgenerator with 'yield from'
    yield from subgenerator2()

    print(" ")
    tbprint("gen", "D")

    hprint("main gen stop")


def main() -> None:
    foo = main_generator()

    for k in foo:
        tbprint("main", "--->", k)


if __name__ == "__main__":
    main()
