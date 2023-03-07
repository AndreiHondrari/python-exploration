"""
Concurrent function parts

Let's say we would like to run
111 do foo part 1
222 do bar part 1
AAA do foo part 2
BBB do bar part 2

We can wrap each part as a separate function.
"""


# do foo
def do_foo_part_1():
    print("111")


def do_foo_part_2():
    print("AAA")


# do bar
def do_bar_part_1():
    print("222")


def do_bar_part_2():
    print("BBB")


def main() -> None:
    # Manually select which part of the functionality to execute
    do_foo_part_1()
    do_bar_part_1()
    do_foo_part_2()
    do_bar_part_2()


if __name__ == "__main__":
    main()
