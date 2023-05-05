class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# if the previous number < 0 do nothing;
# if the previous number > 0 add the current number;
# find the max in the update array
#e.g. [-2,1,-3,4,-1,2,1,-5,4]->[-1,-2,4,3,5,6,1,5]
