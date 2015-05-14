
def f():
	return 1,2,3

(a,b,c) = f()

print a
print b
print c

print tuple(f())
print list(f())

x, y = f()
print x
print y