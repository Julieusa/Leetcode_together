class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target<=nums[0]:
            return 0
        else:
            if target<=nums[-1]:
                for i in range(len(nums)-1):
                    if nums[i]<target and nums[i+1]>=target:
                        #if nums[i+1]==target:
                        return i+1
            else:
                return len(nums)
                
                
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range (len(nums)+1):
            if i==len(nums) or nums[i]>=target:
                return i
            
