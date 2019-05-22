"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from typing import Set
from itertools import count

from ut import p


def prime_factors(n: int) -> Set[int]:
    factors = []
    current_dividend = n
    no_more_divisors = False

    while True:
        counter = count(start=2, step=1)

        while True:
            divisor = next(counter)

            if divisor >= current_dividend:
                no_more_divisors = True
                factors.append(divisor)
                break

            if current_dividend % divisor == 0:
                current_dividend //= divisor
                factors.append(divisor)
                break

        if no_more_divisors:
            break

    return set(factors)


def show_it(n: int) -> None:
    factors = sorted(prime_factors(n))
    print(f"{n} -> {factors} | {max(factors)}")


p("Prime factors")

show_it(8)
show_it(13195)
show_it(600851475143)
