#!python3

from ut import p

p("from pack1 import pmod1")

pkg = __import__("pack1.pmod1", fromlist=['pmod1'])
print("pkg", pkg)

pkg.pmod1_something()
pkg.pmod1_otherthing()
