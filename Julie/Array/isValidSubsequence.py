def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx +=1 #Once matched with array value, move to the next target
		arrIdx +=1 
	return seqIdx == len(sequence)

# use two index variables to help comparing 
# Because the subsequence suppose to have the same order, the arrIdx just keep moving to the next element.

def isValidSubsequence(array, sequence):
	seqIdx = 0
	for value in array:
		if seqIdx == len(sequece): # finished loop over the sequence
			break # jump out the loop
		if sequence[seqIdx] == value:
			seqIdx += 1
	return seqIdx == len(sequence)

