#!python3

from ut import p
import functools

def dec1(f):
    def wrapper():
        f()

    return wrapper

p("----> update_wrapper <----")
def dec2(f):

    def wrapper():
        f()

    wrapper = functools.update_wrapper(wrapper, f)
    return wrapper

def somef():
    '''THIS IS SOME F... does something !'''
    print("SOME F")

p("somef no decoration")
print("NAME 1", somef.__name__)
print("DOC 1", somef.__doc__)

p("somef simple decoration")
wrapped_somef_1 = dec1(somef)
print("NAME 2", wrapped_somef_1.__name__)
print("DOC 2", wrapped_somef_1.__doc__)

p("somef decoration with update_wrapper usage")
wrapped_somef_2 = dec2(somef)
print("NAME 3", wrapped_somef_2.__name__)
print("DOC 3", wrapped_somef_2.__doc__)

p("----> wraps <----")
def dec3(f):

    @functools.wraps(f)
    def wrapper():
        f()

    return wrapper

def somef2():
    '''THIS IS SOME F... does something !'''
    print("WRAPS F")

p("somef2 no decoration")
print("NAME 1", somef2.__name__)
print("DOC 1", somef2.__doc__)

p("somef2 simple decoration")
wrapped_somef2_1 = dec1(somef2)
print("NAME 2", wrapped_somef2_1.__name__)
print("DOC 2", wrapped_somef2_1.__doc__)

p("somef2 decoration with update_wrapper usage")
wrapped_somef2_2 = dec3(somef2)
print("NAME 3", wrapped_somef2_2.__name__)
print("DOC 3", wrapped_somef2_2.__doc__)