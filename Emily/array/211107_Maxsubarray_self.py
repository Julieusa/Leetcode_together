class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if max(nums)<=0:
            return max(nums)
        else:
            sum_=0
            pointer=0
            array1=[]
            while pointer<len(nums):
                if nums[pointer]>0:
                    sum_=nums[pointer]+sum_
                    array1.append(sum_)
                else:
                    compar=nums[pointer]+sum_
                    if compar<=0:
                        compar=0
                        sum_=0
                    else:
                        sum_=compar
                pointer+=1      
            return max(array1)
          
          #store the postive integer summation into array, and select the maximum
