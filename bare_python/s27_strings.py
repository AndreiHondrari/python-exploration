#!python

from ut import *
from string import *

# Many string functions that were available in Python 2.0 were considered
# deprecated in Python 2.x while in Python 3.x they were
# removed completely and made available under str.
# a list of such functions:
# atof, atoi, atol, capitalize, lower, upper, expandtabs
# find, rfind, index, rindex, count, rsplit, splitfields,
# join, joinfields, lstrip, rstrip, strip, swapcase, translate,
# ljust, rjust, center, zfill, replace

p("str in str")
print("cartof" in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf")
print("cartof" not in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf")
print("ZZZZ" not in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf")

p('capitalize')
# print(capitalize('zzZzzzZzz'))  # -> no longer available in Python 3
print('zzZzzzZzz yTYyyYY'.capitalize())  # capitalize() deprecated in favor of str.capitalize()

p('upper')
# print(upper('zzAdddWAddwWw'))
print('zzAdddWAddwWw'.upper())  # upper() deprecated in favor of str.upper()

p('lower')
# print(lower('zzAdddWAddwWw'))
print('zzAdddWAddwWw'.lower())  # lower() deprecated in favor of str.lower()

p('find')
print('aaabbbbzvvvvzzdwadadwq'.find('zz'))
print('aaabbbbzvvvvzzdwadadwq'.find('cc'))

p('join')
# print(join(["dwada", "zz zz"]))  # no longer available in Python 3
print(" $ ".join(['stalin', 'lenin', 'gorbaciov', 'strontin']))

p('split')
print("adwadwpjo%dwjaodoaj%djwdjapj".split('%'))

p('format')
print('strontin {{0:.2f}}: {0:.2f}'.format(421.555))
print('strontin {{0:.2e}}: {0:.2e}'.format(421.555))
print('strontin {{0:*20}}: {0:*>20}'.format(222))
print('strontin {{0:*>20}}: {0:*>20}'.format(222))
print('strontin {{0:*^20}}: {0:*^20}'.format(222))
print('strontin {{0:*=20}}: {0:*=20}'.format(222))
print('strontin {{0:*<20}}: {0:*<20}'.format(222))
print('strontin {{0:->20}}: {0:->20}'.format(222)) #  --> how to fill with minus
print('{0:,}'.format(100000000000000))

p('replace')
print("cartofZZZdawdwa".replace('ZZZ', "   SOMETHIGN ELSE    "))

p('templates')
t = Template("something $ADJ")
print(t.substitute(ADJ="great"))
print(t.substitute(ADJ="nice"))
print(t.substitute(ADJ="extraodinary"))

p("format differently types")
for i in range(10):
    print("{:0>8b}".format(i))

print("{:.0%}".format(0.242))

p("named format args")
print("{cartof}".format(cartof=42421))
