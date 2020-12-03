#  angry children

N = input()
K = input()

lst = []

if N >= 1 and N <= 10**5 and K >= 1 and K <= N:
    for i in range(N):
        lst.append(input())


    lst = filter(lambda c: c >= 0 and c <= 10**9, lst)

    min_lst = []
    for i in range(K):
        minval = min(lst)
        lst.remove(minval)
        min_lst.append(minval)

    print(max(min_lst) - min(min_lst))

