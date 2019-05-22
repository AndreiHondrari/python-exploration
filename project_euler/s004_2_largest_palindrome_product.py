"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from collections import namedtuple

Palindrome = namedtuple("Palindrome", ["n", "a", "b"])


def reverse_number(n: int) -> int:
    reversed = 0
    while n > 0:
        last_digit = n % 10
        reversed = reversed * 10 + last_digit
        n = n // 10
    return reversed


def is_palindrome(n: int) -> bool:
    return n == reverse_number(n)


largest_palindrome = None
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        n = i * j

        # a * b will produces numbers that are lower than the
        # current detected largest palindrome
        if largest_palindrome is not None and n <= largest_palindrome.n:
            break

        # initialize if the palindrome is detected
        # or just update it if it's no longer the largest
        if (
            is_palindrome(n) and (
                largest_palindrome is None or largest_palindrome.n < n
            )
        ):
            largest_palindrome = Palindrome(n=n, a=i, b=j)

if largest_palindrome is not None:
    print(f"Largest palindrome: {largest_palindrome}")
else:
    print("No palindrome found!")
