## Three number sum

def threeNumberSum(array, targetSum):
	array.sort()
	output = []
	for i in range(len(array)):
		element1 = array[i]
		# print("the first loop is",element1)
		TwoSum = targetSum-element1
		for j in range(i+1, len(array)):
			element2 = array[j]
			# print("the second loop is",element2)
			for k in range(j+1, len(array)):
				element3 = array[k]
				# print("the third loop is",element3)
				if element2 + element3 == TwoSum:
					output.append( [element1, element2, element3] )
	return output
	
### Issue need to be solved while coding:
* how to avoid repeat value? use i+1, j+1. use print to make sure the loop is right
* how to the triplets ordered in a ascending order? sort the array in the begining
* how to store the tripliets in the array? use append for the list
