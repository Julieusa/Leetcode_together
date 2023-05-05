# O(nm) time| O(mn) space, use matrix to store 
def levenshteinDistance(str1, str2):
	#create a 2 dimensional array: col=len(str1)+1, row = len(str2)+1
	edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	# first column, (0,0) element is 0
	for i in range(1, len(str2) + 1):
		edits[i][0] = edits[i-1][0] + 1
	# other columns
	for i in range(1, len(str2) +1):
		for j in range(1, len(str1)+ 1):
			if str2[i-1] == str1[j-1]:
				edits[i][j] = edits[i-1][j-1]
			else:
				edits[i][j] = 1 + min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1])
	return edits[-1][-1]


# O(nm) time| O(min(m,n)) space, actually we only need to store the last two rows 

def levenshteinDistance(str1, str2):
	# instead storing the whole matrix, we actually only need to store the last two row.
	small = str1 if len(str1) < len(str2) else str2 # shorter string 
	big = str1 if len(str1) >= len(str2) else str2 # longer string 
	evenEdits = [x for x in range(len(small) + 1)] # even row, initialize [0,1,2,3...]. want smallest column to ultimate space, so we use small here 
	oddEdits = [None for x in range(len(small) +1)] #odd row
	
	
	for i in range(1, len(big) + 1):
		# find which case is for currentEdits
		if i % 2 == 1:
			currentEdits = oddEdits
			previousEdits = evenEdits
		else:
			currentEdits = evenEdits
			previousEdits = oddEdits
		currentEdits[0] = i   #since first column is [0,1,2,3,4...]
		for j in range(1, len(small) + 1):
			if big[i-1] == small[j-1]:
				currentEdits[j] = previousEdits[j-1]
			else:
				currentEdits[j] = 1 + min(previousEdits[j-1], previousEdits[j], currentEdits[j-1])
	return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]
