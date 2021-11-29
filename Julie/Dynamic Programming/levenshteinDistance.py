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
