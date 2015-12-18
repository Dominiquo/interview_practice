def compress(string):
	compressed = []
	prev_char = None
	count = 1
	for i in range(len(string)):
		current_char = string[i]
		if current_char == prev_char:
			count += 1
		else:
			if count != 1:
				compressed.append(str(count))
			count = 1
			compressed.append(current_char)
		prev_char = current_char
	if count!=1:
		compressed.append(str(count))
	return ''.join(compressed)



print compress("aabb")

