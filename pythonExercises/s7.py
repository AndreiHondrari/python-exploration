# lonely integer

N = input()
lst = raw_input()
lst = lst.split(' ')
lst = map(int, lst)

if N == len(lst) and N % 2 == 1:
	lst = filter(lambda x: x>=0 and x<=100, lst)
	lstset = set(lst)

	counts = {}
	for x in lstset:
		counts[x] = lst.count(x)

	print [k for k,v in counts.items() if v == 1][0]
