#!python

from ut import p
import functools

p("partial")
def myf(x, y):
    print(x+y)

myfp = functools.partial(myf, y=3)
myfp(10)



def dec1(f):
    def wrapper():
        f()

    return wrapper

p("update_wrapper")

def dec2(f):

    def wrapper():
        f()

    wrapper = functools.update_wrapper(wrapper, f)
    return wrapper

def somef2():
    '''THIS IS SOME F... does something !'''
    print("WRAPS F")

print("NAME 1", somef2.__name__)
print("DOC 1", somef2.__doc__)

wrapped_somef2_1 = dec1(somef2)
print("NAME 2", wrapped_somef2_1.__name__)
print("DOC 2", wrapped_somef2_1.__doc__)

wrapped_somef2_2 = dec2(somef2)
print("NAME 3", wrapped_somef2_2.__name__)
print("DOC 3", wrapped_somef2_2.__doc__)

p("wraps")

def dec3(f):

    @functools.wraps(f)
    def wrapper():
        f()

    return wrapper

def somef2():
    '''THIS IS SOME F... does something !'''
    print("WRAPS F")

print("NAME 1", somef2.__name__)
print("DOC 1", somef2.__doc__)

wrapped_somef2_1 = dec1(somef2)
print("NAME 2", wrapped_somef2_1.__name__)
print("DOC 2", wrapped_somef2_1.__doc__)

wrapped_somef2_2 = dec3(somef2)
print("NAME 3", wrapped_somef2_2.__name__)
print("DOC 3", wrapped_somef2_2.__doc__)