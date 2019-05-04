#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class AbstractItem:
    pass

    def __str__(self):
        return self.__class__.__name__ + ": " + str(id(self))


class AbstractItem1(AbstractItem):
    pass


class ConcreteItemA(AbstractItem1):
    pass


class ConcreteItemB(AbstractItem1):
    pass


class AbstractItem2(AbstractItem):
    pass


class ConcreteItemC(AbstractItem2):
    pass


class AbstractBuilder:
    __metaclass__ = ABCMeta

    items = []

    @abstractmethod
    def buildMix1(self):
        raise NotImplemented()

    @abstractmethod
    def buildMix2(self):
        raise NotImplemented()

    def getResult(self):
        return self.items


class ConcreteBuilder1(AbstractBuilder):
    pass 

    def buildMix1(self):
        self.items = []
        self.items.append(ConcreteItemA())
        self.items.append(ConcreteItemC())

    def buildMix2(self):
        self.items = []
        self.items.append(ConcreteItemB())
        self.items.append(ConcreteItemC())


class ConcreteBuilder2(AbstractBuilder):    
    pass

    def buildMix1(self):
        self.items = []
        self.items.append(ConcreteItemA())
        self.items.append(ConcreteItemC())

    def buildMix2(self):
        self.items = []
        self.items.append(ConcreteItemC())

class Director:

    def __init__(self, builder):
        self.mix1 = None
        self.mix2 = None
        self.builder = builder

    def populateMixes(self):
        self.builder.buildMix1()
        self.mix1 = self.builder.getResult()

        self.builder.buildMix2()
        self.mix2 = self.builder.getResult()


if __name__ != '__main__':
    exit(1)

cb1 = ConcreteBuilder1()
cb2 = ConcreteBuilder2()
d1 = Director(cb1)
d2 = Director(cb2)

d1.populateMixes()
d2.populateMixes()

cmix1 = [ConcreteItemA, ConcreteItemC]
cmix2 = [ConcreteItemB, ConcreteItemC]
cmix3 = [ConcreteItemA, ConcreteItemC]
cmix4 = [ConcreteItemC]

print('\nD1 MIX 1')
for i in d1.mix1:
    print(i)
    assert(i.__class__ in cmix1)

print('\nD1 MIX 2')
for i in d1.mix2:
    print(i)
    assert(i.__class__ in cmix2)

print('\nD2 MIX 1')
for i in d2.mix1:
    print(i)
    assert(i.__class__ in cmix3)

print('\nD2 MIX 2')
for i in d2.mix2:
    print(i)
    assert(i.__class__ in cmix4)

print("\nBUILDER TESTED")