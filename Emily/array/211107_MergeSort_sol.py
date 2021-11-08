class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        
        if n==0 or m==0:            
            for i in range(n):
                nums1[i+m]=nums2[i]
            return nums1
        else:
            k=m-1
            l=n-1
            i=1
            while l>=0:
                if nums1[k]<=nums2[l]:
                    nums1[m+n-i]=nums2[l]
                    l=l-1
                else:
                    nums1[m+n-i]=nums1[k]
                    k=k-1
                    if k==-1:
                        nums1[0:l+1]=nums2[0:l+1]
                        break
                i=i+1
            return nums1
          
          #from back to front
          
  class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:
            # print(i,j,k, nums1)
            # print(nums1[i], nums2[j])
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
        while j >= 0: #deal with the rest after i=-1
            nums1[k] = nums2[j]
            k-=1
            j-=1
