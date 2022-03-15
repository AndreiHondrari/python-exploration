import pkgutil
import pathlib as plib
import functools

hprint = functools.partial(print, "\n# ")


def main() -> None:
    paths = [
        plib.Path().absolute(),
        plib.Path("p1").absolute(),
    ]

    hprint("Paths")
    for p in paths:
        print(p)

    hprint("Walk")
    for x in pkgutil.walk_packages(paths):
        print(x)


if __name__ == "__main__":
    main()
