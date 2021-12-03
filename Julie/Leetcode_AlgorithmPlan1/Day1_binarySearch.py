# Q1: Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right =len(nums) - 1 
     
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot -1
            else:
                left = pivot + 1 
        return -1
  
  
  
#Q2 :You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## A linear scan is a straight forward way but it is slow 
        
#         for i in range(0,n):
#             if (isBadVersion(i)):
#                 return i
            
        # use Binary search, given [1,2,3,...,n], so left and right start from 1 and n
        left = 1
        right =n
        while left < right:
            pivot = left + (right -left)//2 # use // instead / to get int number
            if isBadVersion(pivot) == False:
                left = pivot + 1
            if isBadVersion(pivot) == True:
                right = pivot # use this instead of right = pivot -1, otherwise it will be wrong 
        return left
      
      
      
#Q3 :Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

 def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right :
            pivot = (right+left)//2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot -1
        return left # exactly binary search algorithm, return left index instead of -1 if target not been found 

