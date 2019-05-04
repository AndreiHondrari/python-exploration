#!/usr/bin/python3

print("\nspecific class singleton definition")
class MySingleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySingleton, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        print("MySingleton.__init__ called")

ob1 = MySingleton()
ob2 = MySingleton()

print(id(ob1), id(ob2))

print("\ndecorator singleton definition")

def decorateSingleton(originalClass):

    class SingletonClass(originalClass):

        _instance = None
        _initialized = False

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super(SingletonClass, cls).__new__(cls)

            return cls._instance

        def __init__(self):
            print("SingletonClass.__init__ called")
            if not self._initialized:
                print("SingletonClass initialization")
                super(SingletonClass, self).__init__()

                self._initialized = True

    return SingletonClass

@decorateSingleton
class A:

    def __init__(self):
        print("A.__init__ called")

        self.x = 10

    def __str__(self):
        return str(self.x)

ob3 = A()
ob4 = A()
print(ob3, ob4)
print(id(ob3), id(ob4))

print("\nmetaclass singleton definition")

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if '_instance' not in cls.__dict__:
            cls._instance = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instance

class B:
    __metaclass__ = MetaSingleton

    def __init__(self):
        print("B.__init__ called")

        self.x = 22

    def __str__(self):
        return str(self.x)

ob5 = B()
ob6 = B()
print(ob5, ob6)
print(id(ob5), id(ob6))
