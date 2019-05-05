#!python

import time
from functools import lru_cache

from ut import p

@lru_cache(maxsize=128)
def some(x):
    return sum(range(x))  # --> a time consuming operation (with large x's)

p("wait for it...")

A = 20000000
B = 30000000

p("first run with A")
start = time.time()
some(A)  # --> A
end = time.time()
print(f"{end-start:.2f}s")

p("second run with B")
start = time.time()
some(B)  # --> B
end = time.time()
print(f"{end-start:.2f}s")

p("third run with A")
start = time.time()
some(A)  # --> A
end = time.time()
print(f"{end-start:.2f}s --> obviously faster this time because it used the cached value")

p("Explore the cache info")
print(some.cache_info())

p("Clear the cache")
some.cache_clear()

p("fourth run with A")
start = time.time()
some(A)  # --> A
end = time.time()
print(f"{end-start:.2f}s --> this time slower as the first time because of the cache clear")