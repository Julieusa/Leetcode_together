def nonConstructibleChange(coins):
    coins.sort()
	#print(coins)
	
	currentChangeCreated = 0
	for coin in coins:
		if coin > currentChangeCreated + 1: # start case:if最小的coin都比1大, jump out
			                                # key part for the loop end
			return currentChangeCreated + 1
		
		currentChangeCreated += coin
		#print(currentChangeCreated)
		
    return currentChangeCreated + 1 
### why? if the current coin is greater than `change + 1`
###the smallest impossible change is equal to `change + 1`
