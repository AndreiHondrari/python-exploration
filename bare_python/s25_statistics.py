#!python3

import statistics

from ut import p

p("Averages")
print(f"mean: {statistics.mean([1, 5])}")
print(f"median: {statistics.median([1, 5])}")
print(f"mode: {statistics.mode([1, 1, 1, 5, 5, 5, 5])}")

p("Spread")
print(f"pvariance (s**2 = sum(xi - xmean) / n - 1) where n is the sample size: {statistics.pvariance([1, 2, 3])}")