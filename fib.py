import time

def f(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib(n):
	if n == 0:
		return 0
	elif n < 3:
		return 1
	else:
		return fib(n-1) + fib(n-2)

start = time.clock()
f(40)
print 'iterative process takes',time.clock()-start


#aka really slow version
start = time.clock()
fib(40)
print 'recursive non memoization method takes', time.clock() - start