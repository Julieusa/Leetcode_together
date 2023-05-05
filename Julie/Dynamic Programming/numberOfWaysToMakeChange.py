# find the number of ways to make change by given amount and coins
def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amount in range(n+1)]
	ways[0]=1
	for denom in denoms:
		for amount in range(1, n+1):
			if denom <= amount: 
				ways[amount] += ways[amount-denom]  #key
	return ways[n]



# find the minimum number of coins needed to make a change 
def minNumberOfCoinsForChange(n, denoms):
	numOfCoins = [float("inf") for amount in range(n+1)]
	numOfCoins[0] = 0
	for denom in denoms:
		for amount in range(len(numOfCoins)):
			if denom <= amount:
				numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1 )
	return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


# Compare these two questions, the second question is based on the idea of the first one
