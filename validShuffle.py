def getPermutations(word):
	if len(word) == 1:
		return [word]

	permuations = getPermutations(word[1:])
	character = word[0]
	result = []

	for perm in permuations:
		for i in range(len(perm)+1):
			result.append(perm[:i]+character+perm[i:])

	return result


print getPermutations('abc')