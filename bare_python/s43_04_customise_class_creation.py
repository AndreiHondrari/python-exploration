
from ut import p

p("Basic class customisation - arguments exploration")

class A:

    def __new__(cls, *args, **kwargs):
        new_instance = super().__new__(cls)
        print(f"A.__new__ args: {args}")
        print(f"A.__new__ kwargs: {kwargs}")
        return new_instance

    def __init__(self, *args, **kwargs):
        print(f"A.__init__ args: {args}")
        print(f"A.__init__ kwargs: {kwargs}")

    def __del__(cls):
        print(f"A.__del__")

a_inst = A('positional-arg', some_named_arg=123)
del a_inst

p("Basic subclass initialization")
# it never takes positional arguments
# because it is impossible to pass them in the
# base classes declaration
# SomeClass(Base1, ..kwargs) -> no args

class Base1:
    def __init_subclass__(subclass, x_arg, **kwargs):
        super().__init_subclass__(**kwargs)
        # kwarg x_arg mapped to positional arg x_arg
        print(f"Base1.__init__subclass__ x_arg: {x_arg}")

        # kwargs has the x_arg popped out
        print(f"Base1.__init__subclass__ kwargs: {kwargs}")

class B(Base1, x_arg=111):
    pass

p("Subclass initialization kwargs to positional arg mapping")
# demonstrate that compared to the regulat subclass init
# the metaclass could not map the kwarg to an arg

try:
    class C(Base1, y_arg=222):
        pass
except TypeError:
    print("-> TypeError caught for C(Base1, y_arg=222)")
    # the reason is that the metaclass could not
    # map the y_arg kwarg to any positional argument
    # of the same name hence it kept it in kwargs
    # and passed it further where we used it with
    # super().__init_subclass__.
    # TypeError comes from object.__init_subclass__(cls)
    # which does not accept any args or kwargs

p("Subclass initialization with multiple bases")
class Base2:
    def __init_subclass__(subclass, y_arg, **kwargs):
        super().__init_subclass__(**kwargs)
        # kwarg y_arg mapped to positional arg y_arg
        print(f"Base2.__init__subclass__ y_arg: {y_arg}")

        # kwargs has the x_arg popped out
        print(f"Base2.__init__subclass__ kwargs: {kwargs}")


# order of the named arguments does not matter
class D(Base2, Base1, x_arg=111, y_arg=222):
    pass


p("Metaclass customisation")

class Base3:
    pass

class Base4:

    def __init_subclass__(subclass, **kwargs):
        print(f"Base4.__init__subclass__ kwargs: {kwargs}")

class Metaclass1(type):

    def __prepare__(name, bases, *args, **kwargs):
        print(f"Metaclass1.__prepare__ name: {name}")
        print(f"Metaclass1.__prepare__ bases: {bases}")
        print(f"Metaclass1.__prepare__ args: {args}")
        print(f"Metaclass1.__prepare__ kwargs: {kwargs}")
        return {
            'prepare_named_arg': 333
        }

    def __new__(cls, name, bases, namespace, *args, **kwargs):
        print(f"Metaclass1.__new__ cls: {cls}")
        print(f"Metaclass1.__new__ name: {name}")
        print(f"Metaclass1.__new__ bases: {bases}")
        print(f"Metaclass1.__new__ namespace: {namespace}")
        print(f"Metaclass1.__new__ args: {args}")
        print(f"Metaclass1.__new__ kwargs: {kwargs}")
        return super().__new__(cls, name, bases, namespace)

    def __init__(self, name, bases, namespace, *args, **kwargs):
        print(f"Metaclass1.__init__ name: {name}")
        print(f"Metaclass1.__init__ bases: {bases}")
        print(f"Metaclass1.__init__ namespace: {namespace}")
        print(f"Metaclass1.__init__ args: {args}")
        print(f"Metaclass1.__init__ kwargs: {kwargs}")

class E(Base4, Base3, metaclass=Metaclass1, x=555555):
    pass
