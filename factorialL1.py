def factorial(n):
	current = 1
	while n > 0:
		counter = 0
		value = current
		while counter < n-1:
			current += value
			counter += 1
		n -= 1

	return current

print factorial(3)