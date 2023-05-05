class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        i=j=0
        array1=[]

        while i<len(nums1):
            if nums1[i]==nums2[j]:
                array1.append(nums1[i])
                nums2[j]=1001
                if len(array1)==min(len(nums1),len(nums2)):
                    break
                else:
                    i+=1
                    j=0
            else:
                j=j+1
                if j==len(nums2):
                    i=i+1
                    j=0
    
                
        return array1
        """
        #slow 
        #replace the repeated by 1001 (max number)

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
            #print(counts)
#return {1: 1}
#{1: 1, 2: 1}
#{1: 1, 2: 2}
#{1: 2, 2: 2} counts for each member. If dict.get(5,0), if no 5 existed in the dictory, then return 0, if exist, return the corresponding value.

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res
