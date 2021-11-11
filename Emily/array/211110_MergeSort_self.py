class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """    
        #two pointer compared backwards
        fast=m-1
        slow=n-1
        while slow>=0 and fast>=0:
            if nums1[fast]<=nums2[slow]:
                nums1[slow+fast+1]=nums2[slow]
                slow-=1
                
            else:
                nums1[slow+fast+1]=nums1[fast]
                fast-=1
        #Now nums1 should be ready if the first element in nums2 is bigger than first element in nums1, if not, then append the sorted small num2 to num1
        if fast==-1:
            nums1[0:slow+1]=nums2[0:slow+1]
        return nums1
