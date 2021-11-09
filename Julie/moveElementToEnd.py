##You are given an array of integers and an integer. Write a function that moves all instances of that integer in the array 
## to the end of the array and returns the array.
## It doesn't need to maintain the order of the other integers. 

def moveElementToEnd(array, toMove):
	i=0
	j=len(array)-1
	while i<j:
		while i<j and array[j] == toMove:
			j-=1
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i] # swap two element
		i +=1
			
	return array
