#O(n^2) time
# def arrayOfProducts(array):
# 	output = []
# 	prod =1
# 	for i in range(len(array)):
# 		ar = takeOutIdx(i, array)
# 		prod= product(ar)
# 		output.append(prod)
# 	return output

# def takeOutIdx(Idx, array):
# 	newArray=[]
# 	for i in range(len(array)):
# 		if i!=Idx:
# 			newArray.append(array[i])
# 	return newArray
			
# def product(array):
# 	prod=1
# 	for element in array:
# 		prod = prod*element
# 	return prod

# or just use one function
def arrayOfProducts(array):
	products = [1 for _ in range(len(array))] #create same length array with all 1
	
	for i in range(len(array)):
		runningProduct=1 # nedd to reset running product as 1 before starting to calculate the product
		                 # I forgot this part before so I have to use a function to aviod error
		for j in range(len(array)):
			if i!=j:
				runningProduct *= array[j]
		products[i] = runningProduct
	
	return products


###### O(n) time, O(n) space
def arrayOfProducts(array):
	products = [1 for _ in range(len(array))] 
	leftProducts = [1 for _ in range(len(array))] 
	rightProducts = [1 for _ in range(len(array))] 
	
	leftRunningProduct = 1
	for i in range(len(array)):
		leftProducts[i]=leftRunningProduct
		leftRunningProduct *= array[i]
	print(leftProducts)
		
	rightRunningProduct =1
	for i in reversed(range(len(array))):
		rightProducts[i]=rightRunningProduct
		rightRunningProduct *= array[i]
	
		
	for i in range(len(array)):
		products[i]=leftProducts[i]*rightProducts[i]
		
	return products

###### O(n) space, O(n) time 
def arrayOfProducts(array):
	products = [1 for _ in range(len(array))]
	
	leftRunningProduct =1
	for i in range(len(array)):
		products[i] = leftRunningProduct
		leftRunningProduct *= array[i]
		
		rightRunningProduct =1
	for i in reversed(range(len(array))):
		products[i] *= rightRunningProduct
		rightRunningProduct *= array[i]

	return products

# The difference from solution 2 is : This one doesn't save the left and right product 
# but multipy it dirrect to the array. Saved a little bit space. 
	
	

