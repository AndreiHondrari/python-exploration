

class A:

    def __init__(self, x: int):
        self._x = x
        print(f"Calling A: {x}")


class B:

    def __init__(self, y: int):
        self._y = y
        print(f"Calling B: {y}")


class C(B, A):

    def __init__(self, x: int, y: int):
        A.__init__(self, x)
        B.__init__(self, y)


if __name__ == "__main__":

    c = C(11, 22)
