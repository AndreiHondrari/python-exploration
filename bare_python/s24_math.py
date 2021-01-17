#!python3

import math

from ut import p

p("float constants")
print(f"{math.nan}")
print(f"{math.inf}")
print(f"{-math.inf}")
print(f"pi: {math.pi}")
print(f"e: {math.e}")

p("roundings")
print(f"math.ceil(0.2): {math.ceil(0.2)}")
print(f"math.floor(0.7): {math.floor(0.7)}")