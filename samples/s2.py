#!python3

T = input()

nlst = []

T_MIN = 1
T_MAX = 10
N_MIN = 0
N_MAX = 60

if T >= T_MIN and T <= T_MAX:
    for i in range(T):
        nlst.append(input())

    for n in nlst:
        if n >= N_MIN and n <= N_MAX:
            pass