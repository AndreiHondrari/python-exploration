#!python

# abstract class

from abc import ABCMeta, abstractmethod

class AbstractBase:

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass


class A(AbstractBase):
    pass

ob1 = A()
