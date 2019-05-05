#!python

from ut import p


class A:

    def __enter__(self):
        print("ENTER")

    # (exc_type, exc_value, traceback)
    def __exit__(self, exc_type, exc_value, traceback):
        print("EXIT exc_type", exc_type)
        print("EXIT exc_value", exc_value)
        print("EXIT traceback", traceback)


p("normal context")
with A() as a:
    print("IN WITH")

p("context with exception raised")
try:
    with A() as e:
        raise Exception("some exception")
except Exception:
    print("Exception detected!")

p("return something random")

class B:

    def __enter__(self):
        return 123

    def __exit__(self, *args):
        pass

with B() as x:
    print(x)