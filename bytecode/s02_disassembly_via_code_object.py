import dis
import functools

hprint = functools.partial(print, "#")
eprint = functools.partial(print, end="\n\n")


def f1() -> int:
    x = 10
    y = x * 10
    return y


def main() -> None:
    hprint("f1 code object")
    print("raw", f1.__code__.co_code)
    print(f1.__code__.co_name)
    eprint(f1.__code__.co_varnames)

    hprint("extract bytecode for disassembly")
    f1_bytecode = dis.Bytecode(f1.__code__)
    eprint(f1_bytecode)

    hprint("f1 bytecode info")
    eprint(f1_bytecode.info())

    hprint("f1 bytecode disassembly")
    code_operations = f1_bytecode.dis()
    eprint(code_operations)


if __name__ == "__main__":
    main()
