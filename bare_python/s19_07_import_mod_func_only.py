#!python

from ut import p

p("from mod1 import something")

_temp = __import__("mod1")
something = _temp.something

something()
