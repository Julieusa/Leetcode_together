# Recursive method
# O(2^(n+m)) time | O(n+m) space - n is the width and m is the height
# since last step solution is not stored, each time need see the up and the right 
# so the time complexity is  O(2^(n+m))
def numberOfWaysToTraverseGraph(width, height):
	if width ==1 or height == 1:
		return 1 
	
	return numberOfWaysToTraverseGraph(width-1, height) + numberOfWaysToTraverseGraph(width, height-1)



#Dynamic programming 
# O(n*m) time | O(n*m) space
def numberOfWaysToTraverseGraph(width, height):
	numberOfWays = [[0 for _ in range(width +1 )] for _ in range(height+1)]
	
	for widthIdx in range(1, width + 1):
		for heightIdx in range(1, height + 1):
			if widthIdx == 1 or heightIdx ==1:
				numberOfWays[heightIdx][widthIdx] = 1
			else:
				waysLeft = numberOfWays[heightIdx][widthIdx-1]
				waysUp = numberOfWays[heightIdx-1][widthIdx]
				numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp
	
	return numberOfWays[height][width]



# math : permutations. 
#generate all the permutations of set for down and right
# e.g : {R, R, R, D, D} is the set for graoh with 2 by 3 size
#  all the permutations are 5!/(3! 2!) 
# O(n+m) time | O(1) space, only need to store two variables
def numberOfWaysToTraverseGraph(width, height):
	xDistanceToCorner = width -1 
	yDistanceToCorner = height -1
	
	numerator = factorial(xDistanceToCorner + yDistanceToCorner)
	denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)
	return numerator / denominator

def factorial(num):
	result=1
	
	for n in range(2, num+1):
		result *= n 
		
	return result 
