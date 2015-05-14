import itertools

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

print take(5, (x for x in [1, 2, 3]))

sliced = itertools.islice((x for x in [1, 2, 3]), 5)

print type(sliced)
print sliced