
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

    def newB1():
        raise NotImplemented()

    def newB2():
        raise NotImplemented()

class Base1Factory(AbstractFactory):

    def newA():
        return A1()

    def newB():
        return B1()

class Base2Factory(AbstractFactory):

    def newA():
        return A2()

    def newB():
        return B2()