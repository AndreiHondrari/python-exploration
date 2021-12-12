import importlib


def main() -> None:
    pack1_mod1 = importlib.import_module(".mod1", "pack1")
    pack1_mod1.do_this()  # type: ignore[attr-defined]

    pack2_mod1 = importlib.import_module(".mod1", "pack2")
    pack2_mod1.do_this()  # type: ignore[attr-defined]


if __name__ == '__main__':
    main()
