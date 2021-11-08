def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	OneIdx = 0
	TwoIdx = 0
	smallestDiff =float("inf")
	current =float("inf")
	pair = []
	while OneIdx <= len(arrayOne)-1 and TwoIdx <= len(arrayTwo)-1:
		firstNum =arrayOne[OneIdx]
		secondNum =arrayTwo[TwoIdx]
		if firstNum < secondNum:
			current = secondNum - firstNum
			OneIdx +=1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			TwoIdx +=1
		else:
			return [firstNum, secondNum]
			
		if smallestDiff > current:
			smallestDiff = current
			pair = [firstNum,secondNum]
	return pair
				
 arrayOne= [-1, 5, 10, 20, 28, 3]
 arrayTwo = [26, 134, 135, 15, 17]
