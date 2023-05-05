class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        base_=[[1]*i for i in range(1,numRows+1)]
        
        for m in range(2,numRows):
            for n in range(1,len(base_[m])-1):
                base_[m][n]=base_[m-1][n-1]+base_[m-1][n]
        return base_
      #give a structure set up and altering the numbers, watch out the range in each loop
