"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from typing import Tuple, List
from collections import namedtuple
from operator import attrgetter

Palindrome = namedtuple("Palindrome", ["n", "a", "b"])


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


palindromes = []

for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        n = i * j
        digits_count, digits = get_digits(n)

        if digits_count % 2 == 0:
            middle_lim = digits_count // 2
            first_half = digits[:middle_lim]
            second_half = digits[middle_lim:][::-1]
        else:
            middle_lim = (digits_count - 1) // 2
            first_half = digits[:middle_lim]
            second_half = digits[middle_lim+1:][::-1]

        if first_half == second_half:
            palindromes.append(Palindrome(n=n, a=i, b=j))

max_palindrome = max(palindromes, key=attrgetter('n'))
print(f"Biggest palindrome: {max_palindrome}")
