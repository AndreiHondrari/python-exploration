#!/usr/bin/python

from utils import p 

class CompliantInstance(object):

    def __init__(self):
        self.x = int()
        self.y = int()

    def doXY(self, x, y):
        self.x = x
        self.y = y


class Adaptee(object):

    def __init__(self):
        pass

    def doX(self, X):
        self.x = X

    def doY(self, Y):
        self.y = Y


class AdapteeAdapter(object):

    def __init__(self):
        self.adaptee = Adaptee()

    def doXY(self, x, y):
        self.adaptee.doX(x)
        self.adaptee.doY(y)


class Client(object):

    C_X = 33
    C_Y = 44

    def __init__(self, usedInstance):
        self.used = usedInstance

    def doIt(self):
        self.used.doXY(self.C_X, self.C_Y)


a = AdapteeAdapter()
c = Client(a)
c.doIt()

print a.adaptee.x
print a.adaptee.y

# TODO: make adapter inherited
# TODO: make adapter-adaptee composition with __dict__ adaptation from adapter to adaptee
# TODO: make adapter with aggregation
