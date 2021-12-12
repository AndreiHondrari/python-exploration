import importlib


def main() -> None:
    pack1 = importlib.import_module("pack1")
    pack1.mod1.do_this()  # type: ignore[attr-defined]


if __name__ == '__main__':
    main()
