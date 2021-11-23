# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
	if not len(array): # for empty array
		return 0
	elif len(array) == 1: # for only one element in the array
		return array[0]
	maxSums = array[:] #create a same size array
	maxSums[1] = max(array[0], array[1]) 
	for i in range(2, len(array)):
		maxSums[i] = max(maxSums[i-1], maxSums[i-2]+array[i])
	return maxSums[-1] # return the last number

#################
# No need to store all the max value 
# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
	if not len(array):
		return 0
	elif len(array)==1:
		return array[0]
	first = array[0]
	second = max(array[0], array[1])
	for i in range(2,len(array)):
		current = max(second, first+array[i])
		first = second
		second = current
	return second
