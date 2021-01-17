#!python3

from ut import p

p("import mod1")

pkg = __import__("mod1")
print("pkg", pkg)

pkg.something()
pkg.otherthing()
