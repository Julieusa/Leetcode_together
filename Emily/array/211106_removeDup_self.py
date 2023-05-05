class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)-1):
            if nums[count]==nums[count+1]:
                nums.remove(nums[count])
            else:
                count=count+1
        
        return len(nums)
    
    # use remove function
