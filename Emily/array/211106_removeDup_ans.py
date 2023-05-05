class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        same_=1
        while same_<len(nums):
            if nums[count]==nums[same_]:
                same_=same_+1
            else:
                count=count+1
                nums[count]=nums[same_]
                same_=same_+1
        #print(nums)       
        return count+1    
