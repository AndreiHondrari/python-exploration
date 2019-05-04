#  MAXIMIZING XOR

L = input()
R = input()

results = []

if L >= 1 and R >= L and R <= 10 ** 3:
    for A in xrange(L, R+1):
        for B in xrange(A, R+1):
            results.append(A ^ B)

print(max(results))
