#!python

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(B):
    pass

class F(E):
    pass

class G(F, E):
    pass

print(D.__mro__)
print(F.__mro__)
print(G.__mro__)

