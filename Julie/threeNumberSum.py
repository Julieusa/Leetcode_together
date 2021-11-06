## Three number sum

## O(n^3)
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
# * how to avoid repeat value? use i+1, j+1. use print to make sure the loop is right
# * how to the triplets ordered in a ascending order? sort the array in the begining
# * how to store the tripliets in the array? use append for the list

## O(n^2)
def threeNumberSumOptimal(array, targetSum):
	array.sort()
	output = []
	for i in range(len(array)-2):
		element1 = array[i]
		TwoSum = targetSum - element1
		# print("The current element is ",element1)
		# print("The needed TwoSum", TwoSum)
		left =i+1
		right = len(array) -1
		while left < right:
			# print("The left element is ",array[left])
			# print("The right element is", array[right])
			currentSum = array[left] + array[right]
			# print("The Sum", currentSum)
			if currentSum == TwoSum:
				output.append([element1, array[left], array[right]])
				# break
				left +=1
				right -=1
			elif currentSum < TwoSum:
				left +=1
			elif currentSum > TwoSum:
				right -=1
	return output

#Based on the optimal solution for two number sum. How to stop while and keep searching other solution?
# i in range(len(array)-2) 
# update left +=1 and right -=1 when currentSum==TwoSum, instead of using break.
# If using break, the other potential solution will be omitted
