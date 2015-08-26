import random as rand
import time

def combine(A,B):
	i = 0
	j = 0
	init_len_a = len(A)
	init_len_b = len(B)
 	final = []
	while (i < init_len_a and j < init_len_b):
		if A[0] < B[0]:
			final.append(A.pop(0))
			i += 1
		elif A[0] > B[0]:			
			final.append(B.pop(0))
			j += 1
		else:
			j += 1
			i += 1
			final.append(A.pop(0))
			final.append(B.pop(0))
	if len(A) > 0:
		final = final + A
	elif len(B) > 0:
		final = final + B

	return final


def mergeSort(A):
	if len(A) < 2:
		return A
	else:
		middpoint = len(A)/2
		first_half = A[:middpoint]
		second_half = A[middpoint:]
		return combine(mergeSort(first_half),mergeSort(second_half))
n = 1000
init_list = range(n)
rand.shuffle(init_list)

start = time.time()
mergeSort(init_list)
print 'n =', n, 'in', time.time()-start

# check whether merge sort properly sorts the list it's given
# print all(sorted_list[i] <= sorted_list[i+1] for i in xrange(len(init_list)-1))

