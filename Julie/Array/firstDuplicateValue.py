#O(n^2) time , O(1) space
def firstDuplicateValue(array):
	minimumSecondIdx = len(array)
	for i in range(len(array)):
		value=array[i]
		for j in range(i+1, len(array)):
			valueToCompare = array[j]
			if value==valueToCompare:
				minimumSecondIdx = min(minimumSecondIdx, j)
		
	if minimumSecondIdx == len(array):
		return -1
	
	return array[minimumSecondIdx]

#use a set setrucure
#O(n) time, O(n) space
def firstDuplicateValue(array):
	seen = set()
	for value in array:
		if value in seen:
			return value
		seen.add(value)
		
	return -1
 
 # this is clever, using mapping
# Since the integers are between 1 and the length of the input array, you can 
# map them to indices in the array itself by substracting 1 from them. Once
# you've mapped an integer to an index in the array, you can mutate the value
# in the array at the index and make it negative(by multiplying it by -1). Since 
# the intergers normally aren't negative, the first time that you encounter a negative
# value at the index that an integer maps to, you'll konw that you have already seen that integer.

#O(n) time O(1)space
def firstDuplicateValue(array):
	for value in array:
		absValue = abs(value)
		if array[absValue -1]<0:
			return absValue
		array[absValue-1] *=-1
	return -1
