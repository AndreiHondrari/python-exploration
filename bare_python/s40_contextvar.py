#!python3

from contextvars import ContextVar, Context
from typing import Any, NoReturn, List

import contextvars

name: ContextVar[Any] = ContextVar("name")
contexts: List[Context] = list()


def greet() -> NoReturn:
    print(f"Hello {name.get()}")


# Construct contexts and set the context variable name
for first_name in ["Steve", "Dina", "Harry"]:
    ctx = contextvars.copy_context()
    ctx.run(name.set, first_name)
    contexts.append(ctx)


# Run greet function inside each context
for ctx in reversed(contexts):
    ctx.run(greet)
