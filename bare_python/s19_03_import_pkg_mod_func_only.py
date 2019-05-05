#!python

from ut import p

p("from pack1.pmod1 import pmod1_something")

try:
    pkg = __import__("pack1.pmod1.pmod1_something")
except ModuleNotFoundError as e:
    # raise because pmod1 is not a package and pmod1_something not a module of that "package"
    print(f"raised: {e}")

# the real way to do it is:
_temp = __import__("pack1.pmod1", fromlist=("pmod1",))
pmod1_something = _temp.pmod1_something
pmod1_something()
