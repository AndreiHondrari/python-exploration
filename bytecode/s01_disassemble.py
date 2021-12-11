import dis
import functools

eprint = functools.partial(print, end="\n\n")


def f1() -> int:
    x = 10
    y = x * 10
    return y


def main() -> None:
    print("disassemble")
    dis.dis(f1)
    print()


if __name__ == "__main__":
    main()
