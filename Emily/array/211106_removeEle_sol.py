class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """


        slow=0
        fast=0 
    
        while fast<len(nums):
            if nums[fast]==val:
                fast=fast+1
                #slow=slow+1
            else:
                if nums[slow]!=nums[fast]:
                    nums[slow]=nums[fast]
                fast=fast+1
                slow=slow+1
                    
        return slow
      
      #niubi
