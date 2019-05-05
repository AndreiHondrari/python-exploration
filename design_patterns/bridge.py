#!python

from abc import ABCMeta, abstractmethod

from utils import p


class Implementor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def impOperation(self):
        pass


class ConcreteImplementor1(Implementor):

    def impOperation(self):
        p("CI1")


class ConcreteImplementor2(Implementor):

    def impOperation(self):
        p("CI2")


class Abstraction:
    __metaclass__ = ABCMeta

    @abstractmethod
    def checkImp(self, imp):
        pass

    def __init__(self, imp=None):
        self.checkImp(imp)
        self.imp = imp

    def operation(self):
        self.imp.impOperation()


class Specialization1(Abstraction):
    
    def checkImp(self, imp):
        assert(isinstance(imp, ConcreteImplementor1))

class Specialization2(Abstraction):
    
    def checkImp(self, imp):
        assert(isinstance(imp, ConcreteImplementor2))


imp1 = ConcreteImplementor1()
imp2 = ConcreteImplementor2()

s1 = Specialization1(imp1)
s2 = Specialization2(imp2)

assert(id(s1.imp) == id(imp1))
assert(id(s2.imp) == id(imp2))

s1.operation()
s2.operation()
