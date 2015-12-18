def maxDifference(a):
	minimum,min_i = argMin(a)
	maximum,max_i = argMax(a)
	if len(a) == 0:
		return 0
	current = (0,-1)
	for i in range(len(a)):
		item = a[i]
		if item < maximum and i < max_i:
			diff = maximum - item
			if diff > current[0]:
				current = (diff,i)
		if item > minimum and i > min_i:
			diff = item - minimum
			if diff > current[0]:
				current = (diff,i)
	return current[0]


def argMax(a):
	value,index = (-float('inf'),-1)
	for i in range(len(a)):
		val = a[i]
		if val > value:
			value,index = (val,i)
	return value,index

def argMin(a):
	# value,index
	value,index = (float('inf'),-1)
	for i in range(len(a)):
		val = a[i]
		if val < value:
			value,index = (val,i)
	return value,index


a = [7,9,5,6,3,2]
print a
print maxDifference(a)