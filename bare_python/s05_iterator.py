#!/usr/bin/python3

from ut import p


class MyIter:

    def __init__(self, limit):
        self.x = 10
        self.limit = limit or 0

    def __next__(self):
        tx = self.x

        if tx > self.limit:
            raise StopIteration()

        self.x *= 2

        return tx

    def __iter__(self):  # -> makes this class an iterator class
        return self

a = MyIter(200)

print(type(a))

p("nexting iterator")
while True:
    try:
        print(next(a))  # -> raises StopIteration
    except StopIteration:
        print("StopIteration raised.")
        break

p("foreach iterator")
for x in MyIter(20):
    print(x)