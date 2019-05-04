T = input()

lst = []
results = []

if T >= 1 and T <= 10**4:
    for i in xrange(T):
        lst.append(raw_input())


    lst = filter(lambda x: len(x) >= 1 and len(x) <= 10**4, lst)

    for cst in lst:
        cst = list(cst)
        cstlen = len(cst)
        hcstlen = cstlen / 2
        opct = 0

        limc = ord('a')

        for i in xrange(hcstlen):
            c = ord(cst[i])
            cc = ord(cst[-i-1])

            minc = min(c, cc)
            maxc = max(c, cc)

            for ct in xrange(maxc - minc):
                opct += 1

        results.append(opct)


for v in results:
    print(v)
