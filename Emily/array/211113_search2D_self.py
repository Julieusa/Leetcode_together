class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if matrix[i][-1]>=target:
                for j in range(len(matrix[i])):
                    if matrix[i][j]==target:
                        return True
                    if j==len(matrix[i])-1:
                        return False
            else:
                if i==len(matrix)-1:
                    return False
                  
 #Runtime: 32 ms, faster than 56.27% of Python online submissions for Search a 2D Matrix.
#Memory Usage: 13.9 MB, less than 50.89% of Python online submissions for Search a 2D Matrix.
#O(m+n) yes.
