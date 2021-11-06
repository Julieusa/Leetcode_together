class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    return [i,j]
                  
#Runtime: 3576 ms, faster than 25.73% of Python online submissions for Two Sum.
#Memory Usage: 14.3 MB, less than 48.96% of Python online submissions for Two Sum.
