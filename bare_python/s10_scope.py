#!python

from typing import Callable


def f() -> None:
    lv = 11  # noqa


f()

try:
    print(lv)  # type: ignore
except NameError as e:
    print("[ER] " + str(e))


print("###  this does not change the global variable")
x = 10


def f2() -> None:
    x = 22
    print(x)


f2()
print(x)

print("### set global variable")


def f3() -> None:
    global x
    x = 22


f3()
print(x)

print("### CLOSURES")


def f4() -> Callable[..., None]:

    y = 33

    def f4i() -> None:
        print(y)

    return f4i


f4()()

print("### CLOSURE NAMESPACES")


def f5() -> None:
    f5._mvar = 33  # type: ignore

    def f5i() -> None:
        f5._mvar = 77  # type: ignore

    f5i()
    print(f5._mvar)  # type: ignore


f5.z = 99  # type: ignore
print(f5.z)  # type: ignore

f5()

print("-> WITH INNER NAMESPACE")


def f6() -> None:

    class InnerNamespace:
        pass

    InnerNamespace.mvar = 44  # type: ignore

    def f6i() -> None:
        InnerNamespace.mvar = 99  # type: ignore

    f6i()
    print(InnerNamespace.mvar)  # type: ignore


f6()

print("-> FACTORY OF FUNCTION WITH INNER NAMESPACE")


def f7() -> Callable[..., None]:

    class InnerNamespace:
        pass

    InnerNamespace.mvar = 0  # type: ignore

    def f7i() -> None:
        InnerNamespace.mvar += 11  # type: ignore
        print(InnerNamespace.mvar)  # type: ignore

    return f7i


f7_1 = f7()
f7_1()
f7_1()
f7_1 = f7()
f7_1()
f7_1()
f7_1()
