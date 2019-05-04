#!/usr/bin/python3

class A:

    def __str__(self):
        return "ceva"

    def __repr__(self):
        return "oarece doctring"

a = A()
print(a)
print(repr(a))