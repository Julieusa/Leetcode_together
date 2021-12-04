# Q1 Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
class Solution:
    # O(nlogn) time| O(n) or O(logn) in space
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     for i in range(0,len(nums)):
    #         nums[i] = nums[i]*nums[i]
    #     return sorted(nums)
    
    
    #O(n) time| O(n) space,  using two pointers
    # the biggest square value is either the 1st num or the last num
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left = 0
        right = n-1
        for i in range(n-1, -1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result 
            
        
        
 #Q2: Given an array, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# ### The way I used
#         n = len(nums)
#         for j in range(0,k):
#             result = [0]*n
#             for i in range(0,n-1):
#                 result[0] = nums[n-1]
#                 result[i+1] = nums[i]
#             nums[:] = result
#         nums[:] = result

# # Method 1:The simplest approach is to rotate all the elements of the array in kk steps by rotating the elements by 1 unit in each step.
# # O(nk) time | O(1) space 
# def rotate(self, nums: List[int], k: int) -> None:
#         #speed up the rotation
#         k %= len(nums)
        
#         for i in range(k):
#             previous = nums[-1] # use this interchange variable 
#             for j in range(len(nums)):
#                 nums[j], previous = previous, nums[j]
                
#Method 2: O(n) time | O(n) space
# def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         a = [0]*n
#         for i in range(n):
#             a[(i+k) % n] = num[i]
        
#         nums[:] = a
        
#Method 3:O(n) time | O(1) space
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n 
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break 
            start += 1 




            
        
