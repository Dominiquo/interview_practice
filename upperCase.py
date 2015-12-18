import string

def caseCombos(word):
	combos = []
	if len(word) == 1:
		return [word.capitalize(),word.lower()]
	firstChar = word[0]
	for comb in caseCombos(word[1:]):
		newCap = firstChar.capitalize() + comb
		newLow = firstChar.lower() + comb
		combos.append(newCap)
		combos.append(newLow)
	return combos

print caseCombos("abc")