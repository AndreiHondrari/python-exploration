#!python3


class A:

    def __delattr__(self, name: str) -> None:
        print("DEL", name)


a = A()
del a.x
