#!/usr/bin/python

class Base1(object):
    pass

class A1(Base1):
    pass

class B1(Base1):
    pass

class Base2(object):
    pass

class A2(Base2):
    pass

class B2(Base2):
    pass

class AbstractFactory(object):

    def newB1(self):
        raise NotImplemented()

    def newB2(self):
        raise NotImplemented()

class Base1Factory(AbstractFactory):

    def newA(self):
        return A1()

    def newB(self):
        return B1()

class Base2Factory(AbstractFactory):

    def newA(self):
        return A2()

    def newB(self):
        return B2()


class FactoryUser(object):
    
    def __init__(self, factory):
        self.factory = factory
        self.a = None
        self.b = None

    def populate(self):
        self.a = self.factory.newA()
        self.b = self.factory.newB()

factory1 = Base1Factory()
factory2 = Base2Factory()

user1 = FactoryUser(factory1)
user2 = FactoryUser(factory2)

user1.populate()
user2.populate()

print isinstance(user1.a, A1)
print isinstance(user1.b, B1)
print isinstance(user2.a, A2)
print isinstance(user2.b, B2)
