
import timeit

class A:
    pass

class B:
    __slots__ = ['x']


def attr_cycle(instance):
    def _attr_cycle():
        instance.x = 33
        instance.x
        del instance.x

    return _attr_cycle

a = A()
b = B()

res1 = timeit.repeat(attr_cycle(a))
res2 = timeit.repeat(attr_cycle(b))

print(min(res1))
print(min(res2))
