class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        else:
            long_array=mat[0]
            for j in range(1,m):
                long_array=long_array+mat[j]
                
            if r==1:
                return [long_array]
            else:
                new_mat=[]
                row=[]
                for i in range(r):
                    row[0:c]=long_array[i*c:(i+1)*c]
                    new_mat.append(row[0:c])
                return new_mat
