#!python3

from ut import p


def reverse_number(n: int) -> int:
    reversed = 0
    while n > 0:
        last_digit = n % 10
        reversed = reversed * 10 + last_digit
        n = n // 10
    return reversed


p("Number reversing")


def show_it(n: int) -> None:
    print(f"{n} -> {reverse_number(n)}")


show_it(1)
show_it(10)
show_it(100)
show_it(98)
show_it(12345)
