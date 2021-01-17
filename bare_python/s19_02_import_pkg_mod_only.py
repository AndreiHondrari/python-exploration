#!python3

from ut import p

p("import pack1 --> but only pmod2 is available from it")
pkg = __import__("pack1.pmod2")

print("pkg", pkg)


try:
    pkg.pmod1
except AttributeError as e:
    print(f"raised: {e}")

pkg.pmod2.pmod2_something()  # actually works
