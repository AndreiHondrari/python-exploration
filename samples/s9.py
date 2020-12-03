#  prng sequence guessing

from collections import namedtuple

N = input()

sequences = {}

TsPair = namedtuple("TimestampsPair", ['t1', 't2'])

if N < 10:
    for i in range(N):
        timestamps = raw_input()
        timestamps = map(int, timestamps.split(' '))
        timestamps = TsPair(t1=timestamps[0], t2=timestamps[1])

        if timestamps[0] - timestamps[1] <= 10**6:
            numbers = []

            for j in range(2):
                numbers.append(input())

            sequences[timestamps] = numbers


    print(sequences)

