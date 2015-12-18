#  split on " ","	",",",":",";","-","."
def  firstRepeatedWord(s):
	# I know this is super clunky, but I don't know regexes off the top of my head and I'm pressed for time
	word_list = s.replace(',',' ').replace(':',' ').replace(';',' ').replace('-',' ').replace('.',' ').split(' ')
	word_set = set([])
	for word in word_list:
		if word not in word_set:
			word_set.add(word)
		else:
			return word
	return ""

print firstRepeatedWord("hey:there")