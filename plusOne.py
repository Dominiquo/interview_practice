# given a list of 1 digit integers, return list of integers representing the full integer +1

def plusOne(A):
	string_integer = ''.join(map(str,A))
	integer_converted = int(string_integer)
	final_integer = integer_converted + 1
	plus_one_string = str(final_integer)
	list_of_strings = list(plus_one_string)

	return map(int,list_of_strings)