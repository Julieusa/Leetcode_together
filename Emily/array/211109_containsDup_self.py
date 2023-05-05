class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        if len(nums)==1:
            return False
        else:
            newarr=sorted(nums)
            for i in range(len(nums)-1):
                if newarr[i]==newarr[i+1]:
                    return True


            if i == len(nums)-1:
                return False
              #Runtime: 92 ms, faster than 92.34% of Python online submissions for Contains Duplicate.
#Memory Usage: 17.3 MB, less than 84.70% of Python online submissions for Contains Duplicate.
