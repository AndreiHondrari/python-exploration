#!python3

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

p("state manipulation")
print("acquire the current random state...")
s1 = getstate()
print(f"{random()}")
print(f"{random()}")
print(f"{random()}")
print("restore the previous state...")
setstate(s1)
print(f"{random()}  --> repeats from here because of state restoration")
print(f"{random()}")
print(f"{random()}")

p("randrange")
print(randrange(10, 16, 2))
print(randrange(10, 16, 2))
print(randrange(10, 16, 2))
print(randrange(10, 16, 2))
print(randrange(10, 16, 2))
print(randrange(10, 16, 2))

