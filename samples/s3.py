#  MAXIMIZING XOR

L = input()
R = input()

results = []

if L >= 1 and R >= L and R <= 10 ** 3:
    for A in range(L, R+1):
        for B in range(A, R+1):
            results.append(A ^ B)

print(max(results))
