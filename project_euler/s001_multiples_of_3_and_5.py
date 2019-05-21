"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from typing import List


def get_multiples(lim: int, references: List[int]) -> List[int]:
    multiples = []

    for n in range(lim):
        if any([n % m_reference == 0 for m_reference in references]):
            multiples.append(n)

    return multiples


multiples = get_multiples(lim=1000, references=[3, 5])

# 233168 is correct for lim=1000
print(sum(multiples))
