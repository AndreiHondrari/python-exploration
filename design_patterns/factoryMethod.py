#!python


class Sample1:
    pass

class Sample2:
    pass

class AbstractCreator():

    def factory(self):
        raise NotImplemented()

    def __init__(self):
        self.sample = self.factory()


class ConcreteCreator1(AbstractCreator):

    def factory(self):
        return Sample1()

class ConcreteCreator2(AbstractCreator):

    def factory(self):
        return Sample2()

c1 = ConcreteCreator1()
c2 = ConcreteCreator2()

print(isinstance(c1.sample, Sample1))
print(isinstance(c2.sample, Sample2))
