#  alternative characters

T = input()

lst = []
results = []

if T >= 1 and T <= 10:
	for i in xrange(T):
		lst.append(raw_input())

	lst = filter(lambda x: len(x) >= 1 and len(x) <= 10**5, lst)

	for cst in lst:
		delct = 0
		
		for j in xrange(len(cst)-1):
			if cst[j] == cst[j+1]:
				delct += 1

		results.append(delct)

for v in results:
	print v
