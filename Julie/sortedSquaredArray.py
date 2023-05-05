# use inside function. O(nlogn) time
def sortedSquaredArray(array):
	squareA = []
	for value in array:
		squareA.append(value*value)
		squareA.sort()
	return squareA

# manual sort. Need to put larger square of abs() in the end
def sortedSquaredArray(array):
	sortedSquare = [0]*len(array) # create a same length zero array
	smallerIdx = 0
	largerIdx = len(array)-1
	for i in reversed(range(len(array))):
		smallerValue = array[smallerIdx]
		largerValue = array[largerIdx]
		if abs(smallerValue) > abs(largerValue):
			sortedSquare[i] = smallerValue*smallerValue
			smallerIdx +=1
			# print(smallerIdx)
		else:
			sortedSquare[i] = largerValue*largerValue
			largerIdx -=1
			# print(largerIdx)
		# print(sortedSquare)
    return sortedSquare
