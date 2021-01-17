#!python3

from typing import List, Tuple

from ut import p


def get_digits(n: int) -> Tuple[int, List[int]]:
    digits: List[int] = []
    digits_count = 1
    digits.append(n % 10)
    n //= 10

    while n != 0:
        digits.append(n % 10)
        n //= 10
        digits_count += 1

    return digits_count, digits[::-1]


p("Get digits")


def show_it(n: int) -> None:
    print(f"{n} -> {get_digits(n)}")


show_it(1)
show_it(10)
show_it(100)
show_it(98)
show_it(12345)
