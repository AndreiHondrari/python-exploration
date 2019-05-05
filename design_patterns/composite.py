#!python

import functools
from abc import ABCMeta, abstractmethod

from utils import p


class AddComponent:

    def __call__(self, component, this):
        assert(isinstance(component, Component))
        assert(isinstance(this, Component))

        this._components[id(component)] = component


class RemoveComponent:

    def __call__(self, component, this):
        assert(isinstance(component, Component))
        assert(isinstance(this, Component))

        this._components.pop(id(component))


class GetChild:

    def __call__(self, n, this):
        assert(isinstance(n, int))
        assert(isinstance(this, Component))

        assert(len(this.components.values()) > n)

        this._components.values()[n]


class Component:
    __metaclass__ = ABCMeta

    def __init__(self):

        if not hasattr(self, '_composite'):
            return

        assert(isinstance(self._composite, bool))

        if not self._composite:
            return

        self._components = {}
        self.addComponent = AddComponent()
        self.addComponent = functools.partial(self.addComponent, this=self)

        self.removeComponent = RemoveComponent()
        self.removeComponent = functools.partial(self.removeComponent, this=self)

        self.getChild = GetChild()
        self.getChild = functools.partial(self.getChild, this=self)

    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):

    def operation(self):
        p("LEAF OPERATION")


class Composite(Component):
    _composite = True

    def operation(self):
        p("COMPOSITE OPERATION")

# LEAFS
p("CREATING LEAVES")
l1 = Leaf()
l2 = Leaf()
l3 = Leaf()

assert(not hasattr(l1, 'addComponent'))
assert(not hasattr(l1, 'removeComponent'))
assert(not hasattr(l1, 'getChild'))
assert(not hasattr(l1, '_components'))

# COMPOSITES
p("CREATING COMPOSITES")
pc = Composite()
c = Composite()
print(pc)
print(c)

assert(callable(pc.addComponent))
assert(callable(pc.removeComponent))
assert(callable(pc.getChild))
assert(isinstance(pc._components, dict))

p("PARENT COMPOSITE INITIALIZATION")
pc.addComponent(l1)
pc.addComponent(c)
print(pc._components)

p("SECONDARY COMPOSITE INITIALIZATION")
c.addComponent(l2)
c.addComponent(l3)
print(c._components)
