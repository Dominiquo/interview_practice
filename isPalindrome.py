def isPalindrome(A):
	# via stack exchange http://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
	stripped_string = ''.join(e for e in A if e.isalnum())
	filtered_string = stripped_string.lower()
	string_len = len(filtered_string)
	if string_len < 2:
		return 1
	for char_index in range(string_len/2):
		is_palindrome = True
		if filtered_string[char_index] != filtered_string[(string_len - 1) - char_index]:
			is_palindrome = False
			break
	return int(is_palindrome)

print isPalindrome("A man, a plan, a canal: Panama")