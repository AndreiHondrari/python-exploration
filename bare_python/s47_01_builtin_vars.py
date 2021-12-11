from ut import p


class X:

    def __init__(self) -> None:
        self.a = 123
        self.b = 567

    def __repr__(self) -> str:
        return f"X({self.__dict__})"


def main() -> None:
    p("Create object")
    x = X()
    print(x)

    p("Dict")
    print(x.__dict__)

    p("Vars")
    print(vars(x))


if __name__ == '__main__':
    main()
