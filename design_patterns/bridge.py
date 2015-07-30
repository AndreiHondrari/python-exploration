#!/usr/bin/python

from abc import ABCMeta, abstractmethod


class Implementor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def impOperation(self):
        pass


class ConcreteImplementor1(Implementor):

    def impOperation(self):
        p("CI1")


class ConcreteImplementor1(Implementor):

    def impOperation(self):
        p("CI2")


class Abstraction(object):

    def __init__(self, imp=None):
        self.imp = imp


class Specialization1(Abstraction):
    pass


class Specialization1(Abstraction):
    pass


imp = Implementor()

s = Specialization1(imp)

assert(id(s.imp) == id(imp))