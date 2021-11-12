# find all the peaks
# find the longest one
def longestPeak(array):
	longestPeakLength = 0
	i=1
	while i < len(array)-1:
		#find isPeak idx
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i+=1
			continue
        #use leftIdx and rightIdx to locate the length
		# the neighborhood already belongs to the peak, so we start from +2 and -2 for the right and left
		leftIdx = i-2 
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
			leftIdx-=1
		rightIdx=i+2
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx]:
			rightIdx+=1
		currentPeakLength = rightIdx - leftIdx -1
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		i = rightIdx
	return longestPeakLength
	
