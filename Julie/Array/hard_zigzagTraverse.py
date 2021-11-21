
=======
###### O(n) time | O(n) space ######

def zigzagTraverse(array):
	height = len(array)-1 # equal to row number
	width = len(array[0])-1 # equal to column number
	result = []
	row, col = 0,0
	goingDown = True
	while not isOutOfBounds(row, col, height, width):
		result.append(array[row][col])
		if goingDown:
			if col == 0 or row == height: # hit the  right border or the bottom border
				goingDown = False
				if row == height:
					col +=1
				else:
					row += 1
			else: # general patern for go down-left
				row += 1
				col -= 1
		else:
			if row == 0 or col == width: # hit the top border or the right border
				goingDown = True
				if col == width:
					row += 1 
				else:
					col += 1 
			else: # general patern for go up-right
				row -= 1
				col += 1 
	return result

def isOutOfBounds(row, col, height, width):
	return row<0 or row>height or col<0 or col>width
					
				
					
		
		
