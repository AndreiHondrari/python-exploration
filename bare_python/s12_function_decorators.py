#!python

from typing import Callable, Any

from ut import p


def fdec(f: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper() -> None:
        print("PRE F")
        f()
        print("POST F")

    return wrapper


print("### direct call of the decorator")


def myf() -> None:
    print("MYF")


fdec(myf)()


print("### syntactic sweet decorator call")


@fdec
def myf2() -> None:
    print("MYF 2")


myf2()


print("### decorator with extra parameters")


def fdec2(param1: Any, param2: Any) -> Callable[..., Any]:

    def innerDecorator(f: Callable[..., Any]) -> Callable[..., Any]:

        def wrapper(fparam1: Any, fparam2: Any) -> None:
            print("PRE F", param1, param2)
            f(fparam1, fparam2)
            print("POST F", param1, param2)

        return wrapper

    return innerDecorator


@fdec2("PARAM1", "PARAM2")
def myf3(a: Any, b: Any) -> None:
    print("MYF 3", a, b)


myf3("FPARAM1", "FPARAM2")


print("### callable instance decorator")


class mycdec:

    def __init__(self, f: Callable[..., Any]):
        self.f = f

    def __call__(self) -> None:
        print("PRE C DEC")
        self.f()
        print("POST C DEC")


@mycdec
def myf4() -> None:
    print("MYF4")


myf4()

print("### callable instance decorator with arguments")


class mycdec:

    def __init__(self, param1: Any, param2: Any):
        pass

    def __call__(self, f: Callable[..., Any]) -> Callable[..., Any]:
        def fwrapper(fparam1: Any) -> None:
            print("PRE C DEC")
            f(fparam1)
            print("POST C DEC")

        return fwrapper


@mycdec("PARAM1", "PARAM2")
def myf4(fparam):
    print("MYF4", fparam)


myf4("FPARAM1")


p("decorator callable with optional keyword-only args (!IMPORTANT)")


def mydec(_func=None, *, bla=None):

    print("BLA", bla)

    def wrapper(functocall):
        print("WRAPPERCALL")
        functocall()

    # this part deals with the manual wrapping depending on
    # the type of decorator call
    if _func is None:
        return wrapper
    else:
        return wrapper(_func)


@mydec
def myf5():
    print("MYF5_1")


@mydec(bla="FLAWFAWFFW")
def myf5():
    print("MYF5_2")
