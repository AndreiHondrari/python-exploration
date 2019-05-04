#!/usr/bin/python3

import copy


class A:
    pass


a = A()
a.lst = [1,2,3]
a.st = "zzzz"

b = copy.copy(a)
a.lst.append(100)
a.st = "wfafw"

print(b.lst)
print(b.st)