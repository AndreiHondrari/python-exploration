#!/usr/bin/python3


class A:

    def __delattr__(self, name):
        print("DEL", name)


a = A()
del a.x
