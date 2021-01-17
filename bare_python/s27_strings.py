#!python3

from ut import p
from string import *

p("str in str")
print("cartof" in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf")
print("cartof" not in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf")
print("ZZZZ" not in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf")

p('capitalize')
print('zzZzzzZzz yTYyyYY'.capitalize())

p('upper')
# print(upper('zzAdddWAddwWw'))
print('zzAdddWAddwWw'.upper())

p('lower')
# print(lower('zzAdddWAddwWw'))
print('zzAdddWAddwWw'.lower())

p('find')
print('aaabbbbzvvvvzzdwadadwq'.find('zz'))
print('aaabbbbzvvvvzzdwadadwq'.find('cc'))

p('join')
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
print('strontin {{0:->20}}: {0:->20}'.format(222))  # -> how to fill with minus
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
