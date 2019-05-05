#!python


def myClassDecorator(OriginalClass):

    class WrapperClass(OriginalClass):

        def __init__(self):
            print("PRE INIT")
            OriginalClass.__init__(self)
            print("POST INIT")

        def ceva(self):
            print("PRE ceva")
            OriginalClass.ceva(self)
            print("POST ceva")

    return WrapperClass


@myClassDecorator
class MyClass:

    def __init__(self):
        print("MCLASS INIT")

    def ceva(self):
        print("MCLASS CEVA")

a = MyClass()

a.ceva()

print("### method decorator")

def mdec(m):

    def wrapper(self):
        print("PRE M")
        m(self)
        print("POST M")

    return wrapper


class A:

    @mdec
    def am(self):
        print("AM")

oba = A()
oba.am()