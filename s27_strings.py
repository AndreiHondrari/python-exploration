from ut import *
from string import *

p("str in str")
print "cartof" in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf"
print "cartof" not in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf"
print "ZZZZ" not in "dwdaw da daw jj()@*$!&()#&! cartof UDW)AA()Wf"

p('capitalize')
print capitalize('zzZzzzZzz')

p('upper')
print upper('zzAdddWAddwWw')

p('lower')
print lower('zzAdddWAddwWw')

p('find')
print 'aaabbbbzvvvvzzdwadadwq'.find('zz')
print 'aaabbbbzvvvvzzdwadadwq'.find('cc')

p('join')
print join(["dwada", "zz zz"])
print " $ ".join(['stalin', 'lenin', 'gorbaciov', 'strontin'])

p('split')
print "adwadwpjo%dwjaodoaj%djwdjapj".split('%')

p('format')
print 'strontin {0:.2f}'.format(421.555)
print 'strontin {0:.2e}'.format(421.555)
print 'strontin {0:*>20}'.format(222)
print 'strontin {0:*^20}'.format(222)
print 'strontin {0:*=20}'.format(222)
print 'strontin {0:*<20}'.format(222)
print '{0:,}'.format(100000000000000)

p('replace')
print "cartofZZZdawdwa".replace('ZZZ', "   SOMETHIGN ELSE    ")

p('templates')
t = Template("something $ADJ")
print t.substitute(ADJ="great")
print t.substitute(ADJ="nice")
print t.substitute(ADJ="extraodinary")

p("format differently types")
for i in xrange(10):
	print "{:0>8b}".format(i)

print "{:.0%}".format(0.242)

p("named format args")
print "{cartof}".format(cartof=42421)