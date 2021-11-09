def nonConstructibleChange(coins):
    coins.sort()
	#print(coins)
	
	currentChangeCreated = 0
	for coin in coins:
		if coin > currentChangeCreated + 1: # start case:if even the smallest coin is larger than 1, then jump out
			                                # key part for ending the loop
			return currentChangeCreated + 1
		
		currentChangeCreated += coin
		#print(currentChangeCreated)
		
    return currentChangeCreated + 1 
### why? if the current coin is greater than `change + 1`
###the smallest impossible change is equal to `change + 1`
