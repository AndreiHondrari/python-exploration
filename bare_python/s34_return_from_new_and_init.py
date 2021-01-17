#!python3

# type: ignore

from __future__ import print_function

import sys

python_version = sys.version_info.major

if python_version < 3:
    print("\n\n!!! ATTENTION! You need to run this with Python 3 !!!\n")
    sys.exit(1)


print("\nreturn something specific from __new__")


class A:

    def __new__(cls):
        print("A.__new__ called")
        return 22

    def __init__(self):
        print("A.__init__ called")  # is actually never called
        # because 22.__init__ is called

    def __str__(self):
        return "THIS IS A"  # is actually never called
        # because 22.__str__ is called


a: A = A()
print(a)


print("\nmimmic original __new__")


class B:

    def __new__(cls):
        print("B.__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("B.__init__ called")

    def __str__(self):
        return "THIS IS B"


print(B())


print("\nnot return anything from __new__")


class C:

    def __new__(cls):
        print("C.__new__ called")
        pass  # do nothing

    def __init__(self):
        print("C.__init__ called")  # is actually never called

    def __str__(self):
        return "THIS IS C"  # is actually never called


print(C())


class Sample:

    def __init__(self):
        print("Sample.__init__ called")

    def __str__(self):
        return "SAMPLE"


print("\nreturn different class instance from __new__")


class D:

    def __new__(cls):
        print("D.__new__ called")
        return Sample()

    def __init__(self):
        print("D.__init__ called")  # is actually never called
        # because Sample.__init__ gets called

    def __str__(self):
        return "THIS IS D"  # is actually never called
        # because Sample.__str__ gets called


print(D())


print("\nreturn from __init__")


class E:

    def __init__(self):
        print("E.__init__ called")
        return 33  # TypeError: __init__ should return None


try:
    print(E())
except TypeError as e:
    print(f"raised: {repr(e)}")
