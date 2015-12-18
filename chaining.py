def solution(A):
	length = len(A)
	if length == 0:
		return -1

	total = float('inf')
	possible = float('inf')
	small_side = float('inf')

	arg_min,min_val = findArgMin(A)
	
	if arg_min > 0 and length > (arg_min  + 1):
		left_neighbor = A[arg_min - 1]
		right_neighbor = A[arg_min + 1]
		possible = left_neighbor + right_neighbor

	if arg_min > 0:
		arg_left,left_val = findArgMin(A[:arg_min])
	else:
		arg_left = -1
		left_val = float('inf')

	if length > (arg_min + 2):
		arg_right, right_val = findArgMin(A[arg_min + 1:])
	else:
		arg_right = -1
		right_val = float('inf')

	if left_val<right_val:
		small_side = left_val
	else:
		small_side = right_val
		
	total = small_side + min_val
	if total < possible:
		return total
	elif possible <= total:
		return possible

	return None



def findArgMin(A):
	length = len(A)
	arg_min = 0
	min_val = A[0]
	for i in range(0,length):
		if A[i] < min_val:
			min_val = A[i]
			arg_min = i

	return (arg_min,min_val)

A = [5, 2, 4, 6, 3, 7]
print A
print solution(A)

print A[2:]
print findArgMin(A[2:])