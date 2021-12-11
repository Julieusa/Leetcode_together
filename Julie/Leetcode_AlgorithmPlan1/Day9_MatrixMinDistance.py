# Use dynamic programming 
# The distance of a cell from 0 can be calculated if we know the nearest distance for all the neighbors, in which case the distance is minimum distance of any neightbor + 1.
# O(r*c) time | O(1) space
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        #why seperate as two part? 
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    top = matrix[i-1][j] if i else float('inf')
                    left = matrix[i][j-1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if cell := matrix[i][j]: #what does this mean? it's the assignment operator in Python. 
                    bottom = matrix[i+1][j] if i < m - 1 else float('inf')
                    right = matrix[i][j+1] if j < n - 1 else float('inf')
                    matrix[i][j] = min(cell, bottom + 1, right + 1)
        return matrix
