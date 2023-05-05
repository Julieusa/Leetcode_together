# Both list.sort() and sorted() have a key parameter to specify a function (or other callable) 
# to be called on each list element prior to making comparisons.

# The value of the key parameter should be a function (or other callable) that 
# takes a single argument and returns a key to use for sorting purposes. 
# This technique is fast because the key function is called exactly once for each input record.
def mergeOverlappingIntervals(intervals):
	sortedIntervals = sorted(intervals, key=lambda x: x[0]) # learn
	
	mergedIntervals = []
	currentInterval = sortedIntervals[0]
	mergedIntervals.append(currentInterval)
	
	for nextInterval in sortedIntervals:
		_, currentIntervalEnd = currentInterval
		nextIntervalStart, nextIntervalEnd = nextInterval
		
		if currentIntervalEnd >= nextIntervalStart:
			currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
		else:
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
			
	return mergedIntervals
