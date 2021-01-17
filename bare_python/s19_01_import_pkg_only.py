#!python3

from ut import p

p("import pack1")
pkg = __import__("pack1")
print("pkg", pkg)

try:
    pkg.pmod1
except AttributeError as e:
    print(f"raised: {e}")
