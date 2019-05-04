#!/usr/bin/python3

print("\nreturn something specific from __new__ in new-style")
class A:

    def __new__(cls):
        print("A.__new__ called")
        return 22

    def __init__(self):
        print("A.__init__ called" ) # is actually never called

    def __str__(self):
        return "THIS IS A"  # is actually never called

print(A())

print("\nreturn something specific from __new__ in old-style")
class B():

    def __new__(cls):
        print("B.__new__ called" ) # is never called because __init__ is the constructor
        return 22

    def __init__(self):
        print("B.__init__ called")

    def __str__(self):
        return "THIS IS B"

print(B())

print("\nreturn something from __init__ in old-style")
class B2():

    def __init__(self):
        print("B2.__init__ called")
        # return 22 -> TypeError: __init__() should return None

    def __str__(self):
        return "THIS IS B2"

print(B2())

print("\nmimmic original __new__ in new-style")
class C:

    def __new__(cls):
        print("C.__new__ called")
        return super(C, cls).__new__(cls)

    def __init__(self):
        print("C.__init__ called")

    def __str__(self):
        return "THIS IS C"

print(C())

print("\nnot return anything from __new__ in new-style")
class D:

    def __new__(cls):
        print("D.__new__ called")
        pass  # do nothing

    def __init__(self):
        print("D.__init__ called" ) # is actually never called

    def __str__(self):
        return "THIS IS D"  # is actually never called

print(D())

class Sample:
    def __str__(self):
        return "SAMPLE"

print("\nreturn different class instance from __new__ in new-style")
class E:

    def __new__(cls):
        print("E.__new__ called")
        return Sample()

    def __init__(self):
        print("E.__init__ called" ) # is actually never called

    def __str__(self):
        return "THIS IS E"  # is actually never called 

print(E())

print("\nreturn from __init__ in new-style")
class F:

    def __init__(self):
        print("F.__init__ called"  )
    #     return 33 # TypeError: __init__ should return None

    def __str__(self):
        return "THIS IS F"  # is actually never called 

print(F())

