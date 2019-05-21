"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from typing import Set
from itertools import count


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


factors = sorted(prime_factors(13195))
factors = sorted(prime_factors(600851475143))
print(factors)
print(max(factors))
