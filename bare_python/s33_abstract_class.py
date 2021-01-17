#!python3

# abstract class

from abc import ABCMeta, abstractmethod, ABC

from ut import p


class AbstractBase(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def some(self):
        print("something")


# replacement for using metaclass=ABCMeta
# --> it already specified it internally
class AbstractBaseSecondary(ABC):

    @abstractmethod
    def some2(self):
        print("something")


class A(AbstractBase):
    pass


class B(AbstractBase):

    def __init__(self):
        pass  # implement the abstractmethod AbstractBase.__init__


class C(AbstractBaseSecondary):
    pass


p("attempt instantiating with abstract AbstractBase.__init__ ...")
try:
    ob1 = A()
except TypeError as e:
    print(f"raised: {repr(e)}")


p("attempt instantiating with abstract AbstractBase.some ...")
try:
    ob2 = B()
except TypeError as e:
    print(f"raised: {repr(e)}")


p("attempt instantiating ABC decendant with abstract "
  "AbstractBaseSecondary.some2 ...")
try:
    ob3 = C()
except TypeError as e:
    print(f"raised: {repr(e)}")
