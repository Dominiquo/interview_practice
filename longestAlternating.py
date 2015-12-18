def solution(A):
	length = len(A)
	if length == 0:
		return 0

	current_longest = 1
	previous_length = 1

	if A[0] == 0:
		prev_treated = 0
	else:
		prev_treated = A[0]/abs(A[0])
	for i in range(1,length):
		previous_val = A[i-1]
		current_value = A[i]

		if current_value != 0:
			current_sign = current_value/abs(current_value)

		if current_value == 0:
			previous_length += 1
			prev_treated = -1*prev_treated

		elif previous_val == 0:
			if prev_treated*current_sign < 0:
				previous_length += 1
				prev_treated = current_sign
			else:
				previous_length = 2

		elif prev_treated*current_sign < 0:
			print "changed sign",i,A[i],"from", prev_treated,"to",prev_treated*-1
			prev_treated = prev_treated*-1

			previous_length += 1
		else:
			previous_val = 1
		if previous_length > current_longest:
			current_longest = previous_length

	return current_longest

print solution(A)