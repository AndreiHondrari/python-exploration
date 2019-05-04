from collections import defaultdict

T = input()

N_LIM_SUP = 10 ** 10
if T >= 1 & T <= 15:
    lst = []
    for i in xrange(T):
        lst.append(input())

    perfect_dividers = defaultdict(list)
    for divided in lst:
        if divided > 0 & divided < N_LIM_SUP:

            p = divided
            dividers = []
            while p > 0.0:
                dividers.append(p % 10)
                p = p / 10

            for divider in dividers:
                if divider <= 0:
                    continue

                result = float(divided) / divider
                if result - int(result) == 0.0:
                    perfect_dividers[divided].append(divider)

    for n in lst:
        print(len(perfect_dividers[n]))
                
            
