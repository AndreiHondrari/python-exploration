"""
Not concurrent

Let's say we would like to run
111 do foo part 1
222 do bar part 1
AAA do foo part 2
BBB do bar part 2

Apparently this is a problem if the execution can not
switch in between functions.
"""


def do_foo():
    print("111")
    print("AAA")


def do_bar():
    print("222")
    print("BBB")


def main() -> None:
    do_foo()
    do_bar()


if __name__ == "__main__":
    main()
