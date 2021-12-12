import importlib


def main() -> None:
    mod1 = importlib.import_module("pack1.mod1")
    mod1.do_this()  # type: ignore[attr-defined]


if __name__ == '__main__':
    main()
