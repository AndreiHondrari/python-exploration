#!python

from ut import p

p("import pack1 --> but only pmod2 is available from it")

pkg = __import__("pack1", fromlist=('pmod2',))  # equivalent 'import pack1 --> but you have access only to pmod1'
print("pkg", pkg)

try:
    pkg.pmod1
except AttributeError as e:
    print(f"raised: {e}")

pkg.pmod2.pmod2_something()  # works because pmod2 is available in the fromlist