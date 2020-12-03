#!python

from ut import *
from collections import *

p("namedtuple")
CartesianCoordinate = namedtuple("CartesianCoordinate", ['x', 'y', 'z'])
cc1 = CartesianCoordinate(10, 20, 30)
print(cc1)
print(f"{{cc1.x}}: {cc1.x}")

print(f"try to assign cc1.x = 44")
try:
    cc1.x = 44
except AttributeError as e:
    print(f"raised: {repr(e)}")


p("regular dict -> not ordered")
d = {}
d['b'] = 10
d['a'] = 22
d[33] = 22

for k, v in d.items():
    print(k, v)

p("list of a dict")
_ = list({'a': 11, 'b': 22})
print(f"list({{'a': 11, 'b': 22}}): {_}")

p("OrderedDict")
od = OrderedDict()
od['b'] = 10
od['a'] = 22
od[33] = 22

for k, v in od.items():
    print(k, v)


p("operations")
print([1,2,3] + [2,3])
print([x for x in [214, 412, 412, 1, 2, 3, 4, 5, 6] if x not in [1,2]])

p("ChainMap")
d1 = {'a': 11, 'b': 22}
d2 = {'b': 33, 'c': 44}
d3 = {'d': 55}

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"d3: {d3}")

print("make a chainmap: ChainMap(d1, d2, d3)")
cm1 = ChainMap(d1, d2, d3)

print(f"cm1: {cm1}")
print(f"cm1.maps: {cm1.maps}")
print(f"cm1.parents: {cm1.parents}")
print(f"cm1['a']: {cm1['a']}")
print(f"cm1['b']: {cm1['b']}  --> always takes the value from the left most map")

p("Example of ChainMap with default values")

default_values = {'something': 77}
values_from_cmd_args_maybe = {'something': 88}

# the idea is that if the key is not in the values from cmd args
# then a default value will be used
_something = ChainMap(values_from_cmd_args_maybe, default_values)['something']
print(f"get the 'something' from the args: {_something}")

# here we use an empty dict
_something = ChainMap({}, default_values)['something']
print(f"get a default 'something': {_something}")

p("Counter as a defaultdict(int)")
cnt = Counter()
some_words = ['apple', 'apple', "gocelyn", "stacy", "stacy", "stacy"]
for w in some_words:
    cnt[w] +=1
print(f"count of {some_words}: {cnt}")

p("Counter as an actual receiver of data")
other_words = ['bla', 'bla', 'aba', 'bla', 'cava']
cnt = Counter(other_words)
print(f"Counter of {other_words}: {cnt}")
print(f"Counter.most_common(2) of {other_words}: {cnt.most_common(2)}")

p("deque (Double-ended Queue) -> can be used as Stack or Queue")
deq = deque()
_OFFSET = 25
print(f"{repr(deq):{_OFFSET}} initial deq")
deq.append(1)
deq.append(2)
deq.append(3)
print(f"{repr(deq):{_OFFSET}} append 1, 2 and 3 to deq")
deq.appendleft(4)
print(f"{repr(deq):{_OFFSET}} appendleft 4 to deq")
deq.pop()
print(f"{repr(deq):{_OFFSET}} pop deq")
deq.popleft()
print(f"{repr(deq):{_OFFSET}} popleft deq")
deq.extend([5, 6])
print(f"{repr(deq):{_OFFSET}} extend with [5, 6] deq")
deq.remove(1)
deq.remove(2)
deq.remove(6)
print(f"{repr(deq):{_OFFSET}} remote 1, 2 and 6 from deq")
deq.extendleft([7, 7])
print(f"{repr(deq):{_OFFSET}} extendleft with [7, 7] deq")
deq.insert(2, 99)
print(f"{repr(deq):{_OFFSET}} insert 99 at 2 deq")
print(f"{str(deq.count(7)):{_OFFSET}} deq.count(7)")
deq.rotate(2)
print(f"{repr(deq):{_OFFSET}} rotate(2) deq")
