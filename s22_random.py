#!/usr/bin/python3

from ut import p
from random import *

p("randint")
print(randint(10, 20))
print(randint(10, 20))
print(randint(10, 20))

p("random")
print(random())
print(random())
print(random())

p("choice")
print(choice([222,333,444,555]))

p("shuffle")
lst = [1,2,3,4]
shuffle(lst)
print(lst)