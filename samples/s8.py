#!/usr/bin/py

def lonelyinteger(lst):
    # lonely integer
    lst = filter(lambda x: x>=0 and x<=100, lst)
    lstset = set(lst)

    counts = {}
    for x in lstset:
        counts[x] = lst.count(x)

    return [k for k,v in counts.items() if v == 1][0]

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    if a == len(b) and a % 2 == 1:
        print(lonelyinteger(b))
