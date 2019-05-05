#!python

from ut import p

from functools import total_ordering


p("define A")
class A:

    def __init__(self, x):
        self.x = x or 0
        print(f"A({x})")


p("define B")
try:
    @total_ordering
    class B:

        def __init__(self, x):
            self.x = x or 0
            print(f"B({x})")

except ValueError as e:
    print(f"raised: {e}")


p("define C")
@total_ordering
class C:

    def __init__(self, x):
        self.x = x or 0
        print(f"C({x})")

    def __lt__(self, other):
        print("LT")
        return self.x < other.x

p("instantiate")
a1 = A(10)
a2 = A(99)

# b1 = B(10)
# b2 = B(99)

c1 = C(10)
c2 = C(99)

p("a1 < a2")
try:
    print(a1 < a2)
except TypeError as e:
    print(f"raised: {e} --> because @total_ordering is not applied on A")

p("c1 == c1")
print(c1 == c1)

p("c1 == c2")
print(c1 == c2)

p("c1 <= c2")
print(c1 <= c2)

p("c1 >= c2")
print(c1 >= c2)

p("c1 < c2")
print(c1 < c2)

p("c1 > c2")
print(c1 > c2)

p(
    """obviously that LT is called everytime because the one operation we defined 
    plus the default __eq__ will be used to interpolate the rest of the operations"""
)
