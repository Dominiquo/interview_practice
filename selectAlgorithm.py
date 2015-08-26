import random
import time

def select(input_list,k):
	start = time.time()
	init_length = len(input_list)

	input_list = list(input_list)
	if not (0 < k < len(input_list)):
		return None
	
	while True:
		pivot = random.choice(input_list)
		left_pivot = []
		right_pivot = []
		pivot_count = 0
		for num in input_list:
			if num < pivot:
				left_pivot.append(num)
			elif num > pivot:
				right_pivot.append(num)
			else:
				pivot_count += 1
		if k < len(left_pivot):
			input_list = left_pivot
		elif k < len(left_pivot) + pivot_count:
			print 'n =',init_length,' in ', time.time()-start
			return pivot
		else:
			input_list = right_pivot
			k -= (len(left_pivot) + pivot_count)


l = range(10000000)
random.shuffle(l)
select(l,63)
