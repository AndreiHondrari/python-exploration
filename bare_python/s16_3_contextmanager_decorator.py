#!python3

from typing import Iterator, Any
from contextlib import contextmanager

from ut import p


@contextmanager
def some_manager(*args: Any, **kwargs: Any) -> Iterator[int]:
    print("acquire resource -> equivalent of __enter__")
    yield 10  # magic that returns the resource to the context handler
    print("release resource -> equivalent of __exit__")


p("cm without exit")
with some_manager() as x:
    print("x", x)


p("cm without exit and raised exception")
try:
    with some_manager():
        raise Exception("potato")
except Exception as e:
    print("potato exception raised")


# full working example
class Resource:

    def do_release(self) -> None:
        print("actual releasing resource")


def acquire_resource() -> Resource:
    return Resource()


def release_resource(resource: Any) -> None:
    resource.do_release()


@contextmanager
def manage_resource(*args: Any, **kwargs: Any) -> Iterator[Any]:
    try:
        print("acquiring resource...")
        resource = acquire_resource()
        yield resource  # magic that returns a resource to the context handler
    finally:
        print("releasing resource...")
        release_resource(resource)


p("full working contextmanager example without exception")
with manage_resource():
    print("potato without exception")

p("full working contextmanager example WITH exception")
try:
    with manage_resource():
        raise Exception("potato")
except Exception:
    print("potato exception raised")

# TODO: explore nullcontext, ExitStack, suppress and other contextlib features.
