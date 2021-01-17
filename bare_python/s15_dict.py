#!python3

from ut import p


class A:
    y = 33

    def __init__(self) -> None:
        self.x = 11

    def show(self) -> None:
        print("self.y", self.x)
        print("__dict__", self.__dict__)


a = A()

p("__dict__")
print("class A.__dict__", A.__dict__)
print("instance a.__dict__", a.__dict__)

p("show")
a.show()

p("vars of instance")
print("vars", vars(a))

p("vars of class")
print("vars", vars(A))

p("key in __dict__")
print("a.__dict__['x']", a.__dict__['x'])

try:
    print("a.__dict__['y']", a.__dict__['y'])
except KeyError:
    # this is the reason why you need to initialize
    # instance attributes in __init__ !
    print("a.__dict__['y'] raises keyError because 'a' is not an instance \
           attribute, rather a class attribute")
