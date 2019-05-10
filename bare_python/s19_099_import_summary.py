#!python

# import pack1
__import__("pack1")

# import pack1 --> only specific module available
pkg = __import__("pack1.pmod2")
pkg = __import__("pack1", fromlist=('pmod2',))  # similar
# pkg.othermod will not work only pmod2

# from pack1.pmod1 import pmod1_something
# __import__("pack1.pmod1.pmod1_something") will NOT work!
_temp = __import__("pack1.pmod1", fromlist=("pmod1",))
pmod1_something = _temp.pmod1_something

# from pack1 import pmod1
__import__("pack1.pmod1", fromlist=('pmod1',))

# import mod1
__import__("mod1")

# from mod1 import something
_temp = __import__("mod1")
something = _temp.something
