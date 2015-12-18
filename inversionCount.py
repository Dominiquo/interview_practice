def combine(A,B):
	inversions = 0
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
			inversions += len(A)
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
	return final,inversions


def mergeSort(A,inversions):
	if len(A) < 2:
		return A,0
	else:
		middpoint = len(A)/2
		first_half = A[:middpoint]
		second_half = A[middpoint:]
		first_half_merge, a = mergeSort(first_half,inversions)
		second_half_merge, b = mergeSort(second_half,inversions)
		combo, c = combine(first_half_merge,second_half_merge)
		return combo, a+b+c

A = [ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]
print mergeSort(A,0)[1]