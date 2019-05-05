#!python

from contextlib import contextmanager

from ut import p


@contextmanager
def some_manager(*args, **kwargs):
    print("acquire resource -> equivalent of __enter__")
    yield 10  # this is the magic that returns the resource to the context handler
    print("release resource -> equivalent of __exit__")

p("cm without exit")
with some_manager() as x:
    print("x", x)


p("cm without exit and raised exception")
try:
    with some_manager():
        raise Exception("potato")
except:
    print("potato exception raised")


# full working example
class Resource:

    def __init__

def acquire_resource():
    return None

def release_resource(resource):
    pass


@contextmanager
def manage_resource(*args, **kwargs):
    try:
        print("acquiring resource...")
        resource = acquire_resource()
        yield resource  # this is the magic that returns the resource to the context handler
    finally:
        print("releasing resource...")
        release_resource(resource)

p("full working contextmanager example without exception")
with some_manager():
    raise Exception("potato")

p("full working contextmanager example WITH exception")
try:
    with some_manager():
        raise Exception("potato")
except:
    print("potato exception raised")

# TODO: explore nullcontext, ExitStack, suppress and other contextlib features.