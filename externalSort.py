def sort_externally(fileA,fileB,block_size):
	file_size = len(fileA)
	pointerA1 = 0
	pointerA2 = pointerA1 + block_size
	pointerB = 0
	finished = False

	if file_size == 0:
		return fileA,fileB
	while not finished:
		end_of_block1 = pointerA2 - 1

		if (pointerA2 + block_size) >= file_size:
			end_of_block2 = file_size - 1
		else:
			end_of_block2 = pointerA2 + block_size - 1
		while (pointerA1 <= end_of_block1) and (pointerA2 <= end_of_block2):
			if fileA[pointerA1] < fileA[pointerA2]:
				fileB[pointerB] = fileA[pointerA1]
				pointerB += 1
				pointerA1 += 1
			elif fileA[pointerA2] < fileA[pointerA1]:
				fileB[pointerB] = fileA[pointerA2]
				pointerB += 1
				pointerA2 += 1
			else:
				fileB[pointerB] = fileA[pointerA1]
				pointerB += 1
				fileB[pointerB] = fileA[pointerA2]
				pointerB += 1
				pointerA1 += 1
				pointerA2 += 1

		if pointerA1 <= end_of_block1:
			while pointerA1 <= end_of_block1:
				fileB[pointerB] = fileA[pointerA1]
				pointerB += 1
				pointerA1 += 1
		elif (pointerA2 <= end_of_block2):
			while (pointerA2 <= end_of_block2):
				fileB[pointerB] = fileA[pointerA2]
				pointerB += 1
				pointerA2 += 1

		if (not(pointerA1 <= end_of_block1) and (not (pointerA2 <= end_of_block2))):
			pointerA1 = end_of_block2 + 1
			pointerA2 = end_of_block2 + block_size + 1

		if pointerA2 > file_size -1:
			end_of_block1 = file_size - 1
			while pointerA1 <= end_of_block1:
				fileB[pointerB] = fileA[pointerA1]
				pointerB += 1
				pointerA1 += 1
			finished = True

	if 2*block_size < file_size:
		sort_externally(fileB,fileA,2*block_size)

	return fileA,fileB


print sort_externally([4,4,2,2,1],[0,0,0,0,0],1)
