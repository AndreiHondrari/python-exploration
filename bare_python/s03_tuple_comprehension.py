#!python

a = (x for x in range(3))

print(next(a))
print(next(a))
print(next(a))

try:
    print(next(a))  # -> raises StopIteration
except StopIteration:
    print("StopIteration raised")
