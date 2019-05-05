#!python

from contextlib import AbstractContextManager as ACM

from ut import p


class A(ACM):

    def __init__(self):
        self.x = 10

    def __exit__(self, *args):
        # needs to be implemented because it's abstract in ACM
        pass


p("ACM normal")
with A() as a:
    print(vars(a))

