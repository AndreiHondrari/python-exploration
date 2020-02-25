

from ut import p


class SomeDescriptor:

    def __init__(self, initial_value=None):
        self._initial_value = initial_value

    def __set_name__(self, obj, name):
        print(f"__set_name__ call: {obj}, {name}")

    def __get__(self, obj, obj_type=None):
        print(f"__get__ call: {obj}: {obj_type}")
        return self._initial_value

    def __set__(self, obj, value):
        print(f"__set__ call: {obj}, {value}")
        self._initial_value = value

    def __delete__(self, obj):
        print(f"__del__ called: {obj}")
        self._initial_value = None


class A:
    x = SomeDescriptor(55)

a1 = A()

p(f"a1.x")
a1.x

p(f"a1.x = 333")
a1.x = 333

p(f"del a1.x")
del a1.x
