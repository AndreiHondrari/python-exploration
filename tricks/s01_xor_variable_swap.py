#!python3

from ut import p

a = 5
b = 9

p("XOR variables swap")
print(f"a: {a} {bin(a)}, b: {b} {bin(b)}\n")

print("a = a XOR b (augment the information in a)")
a = a ^ b
print(f"a: {a} {bin(a)}, b: {b} {bin(b)}\n")

print("b = a XOR b (deaugment in b)")
b = a ^ b
print(f"a: {a} {bin(a)}, b: {b} {bin(b)}\n")

print("a = a XOR b (finally deaugment in a)")
a = a ^ b
print(f"a: {a} {bin(a)}, b: {b} {bin(b)}\n")
