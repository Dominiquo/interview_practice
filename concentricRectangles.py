def row_maker(n,count):
	row = []
	if count == 1:
		return [n]*(2*n -1)
	if count == 1 and n == 1:
		return [1]
	else:
		return [n] + row_maker(n-1,count-1) + [n]
	return row 

def prettyPrint(self,n):
	side_length = 2*n - 1
	num_numbers = []
	array = []
	for num in range(side_length):
		if num <= ((side_length - 1)/2):
			num_numbers.append(num + 1)
		else:
			num_numbers.append(side_length - num)

	for rows in range(side_length):
		numbers_in_row = num_numbers[rows]
		array.append(row_maker(n,numbers_in_row))

	return array


# prettyPrint creates a matrix of concentric rectangles of integers representing its layer in the matrix