# UTOPIAN TREE

T = input()

nlst = []

cycles = {}

if T >= 1 and T <= 10:
	for i in xrange(T):
		nlst.append(input())

	for n in nlst:
		if n >= 0 and n <= 60:

			primary_cycle = True
			cycles[n] = 1
			for i in xrange(n):

				if primary_cycle:
					cycles[n] *= 2
				else:
					cycles[n] += 1

				primary_cycle = not primary_cycle

	for n in nlst:
		print cycles[n]




