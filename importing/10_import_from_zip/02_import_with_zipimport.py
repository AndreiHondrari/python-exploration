import zipimport


def main() -> None:
    z_inst = zipimport.zipimporter("somelib.zip")
    mod1 = z_inst.load_module("mod1")
    mod1.do_something()


if __name__ == "__main__":
    main()
