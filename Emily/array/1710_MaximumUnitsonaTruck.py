class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        box_sort=sorted(boxTypes,key=lambda x: x[1],reverse=True)
        #print(box_sort)
        sum_=0
        size_=0
        index=0
        while size_<truckSize and index<len(box_sort):
            
            size_1=box_sort[index][0]
            value=box_sort[index][1]
            
            if size_+size_1<truckSize:
                sum_=sum_+size_1*value
                
            else:
                sum_=sum_+(truckSize-size_)*value
            #print(index,size_,sum_)
            size_=size_+size_1
            index=index+1
        return sum_
        
        
 #self think
