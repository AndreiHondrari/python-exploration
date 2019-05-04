#!/usr/bin/python3

import inspect


class SampleBase:

    def __init__(self, x=None):
        self.x = x

class Sample1(SampleBase):
    pass


class Sample2(SampleBase):
    pass


class Sample3(SampleBase):
    pass

    
class Sample4(SampleBase):
    pass

    
class Sample5(SampleBase):
    pass


# Concrete factory with fixed factory types

TYPE_1 = 1
TYPE_2 = 2
TYPE_3 = 3

class MyFactory:

    def factory(self, fType):

        assert(fType is not None)

        if fType == TYPE_1:
            return Sample1()

        elif fType == TYPE_2:
            return Sample2()

        elif fType == TYPE_3:
            return Sample3()

print("\nTEST CONCRETE FACTORY WITH FIXED TYPES")
myf = MyFactory()
print(isinstance(myf.factory(TYPE_1), Sample1))
print(isinstance(myf.factory(TYPE_2), Sample2))
print(isinstance(myf.factory(TYPE_3), Sample3))

# Concrete factory with dynamic types

class FactoryTypeAlreadyRegistered(Exception):
    pass


class MyFactory2:

    def __init__(self):
        self.factoryTypes = {}

    def registerType(self, typeIndex, classToRegister):
        assert(typeIndex is not None)
        assert(classToRegister is not None)
        assert(inspect.isclass(classToRegister))

        fClass = self.factoryTypes.get(typeIndex)

        if fClass is not None:
            raise FactoryTypeAlreadyRegistered()

        self.factoryTypes[typeIndex] = classToRegister

    def factory(self, typeIndex, *args, **kwargs):
        assert(typeIndex is not None)

        fClass = self.factoryTypes.get(typeIndex)
        assert(fClass is not None)
        return fClass(*args, **kwargs)


print("\nTEST CONCRETE FACTORY WITH DYNAMIC TYPES")
myf2 = MyFactory2()
myf2.registerType(4, Sample4)
myf2.registerType(5, Sample5)

s1 = myf2.factory(4, x=44)
s2 = myf2.factory(5, x=55)

print(isinstance(s1, Sample4))
print(isinstance(s2, Sample5))
print(s1.x)
print(s2.x)