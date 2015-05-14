
def gen(n):

	x = 0

	while x < n:
		yield x
		x += 1

	# return 0 -> raises SyntaxError (can't have return and yield in a generator function)

a = gen(4)
print a

print a.next()
print a.next()
print a.next()
print a.next()
print a.next()  # -> yields StopIteration
