# 118 119

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        list1=[[1]*i for i in range(rowIndex+2)]
        
        for k in range(2,rowIndex+2):
            for l in range(1,len(list1[k-1])):
                list1[k][l]=list1[k-1][l-1]+list1[k-1][l]
            
        return list1[-1]
      
      
 #memory saving    
 class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        list1=[1]
        
        for k in range(1,rowIndex+1):
            list1=self.dp_alg(k,list1)
        return list1
    
    def dp_alg(self,l,list1):
        if len(list1)<=1:
            list1.append(1)
            return list1
        else:
            list1.append(1)
            for k in range(l-1,0,-1):
                list1[k]=list1[k-1]+list1[k] #[1,2,1,1]->[1,2,3,1]->[1,3,3,1]
            return list1
