
T = input()
N = []

def fib(n, lst=[0, 1]):

    if lst[-1] >= n:
        return lst

    lst.append(lst[-1] + lst[-2])
    return fib(n, lst)

if T >= 1 & T <= 10**5:
    for i in range(T):
        N.append(input())

    for n in N:
        if n >= 1 & n <= 10**10:
            nfib = fib(n)

            if n in nfib:
                print("IsFibo")
            else:
                print("IsNotFibo")