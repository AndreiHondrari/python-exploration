#!python

from ut import p
from fractions import *

F = Fraction
p("Fraction")
fr1 = F('0.2')
print(fr1)
print(fr1.numerator)
print(fr1.denominator)

p("num/den")
fr1 = F(2, 10)
print(fr1)
print(fr1.numerator)
print(fr1.denominator)

p('from float')
print(Fraction.from_float(0.2))