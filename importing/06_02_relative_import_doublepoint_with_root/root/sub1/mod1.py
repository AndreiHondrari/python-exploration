print(f"M1F {__file__}")
print(f"M1N {__name__}")
print(f"M1P {__package__}", end="\n\n")

try:
    from ..sub2 import mod2

    def do_that() -> None:
        print("BLA")
        mod2.do_something()

except ImportError as ierr:
    print("Can't import:", repr(ierr))
