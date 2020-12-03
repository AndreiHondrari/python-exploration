#!python

a = iter([1, 2, 3])  # -> creates and iterator out of that list (listiterator)

print(next(a))
print(next(a))
print(next(a))
print(next(a))  # -> raises StopIteration
