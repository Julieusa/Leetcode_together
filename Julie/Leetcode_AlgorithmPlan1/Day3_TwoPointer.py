# Q1 : Move zeros
#   Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## My way, which is wrong 
        # for i in range(0, len(nums)-1):
        #     if nums[i]==0:
        #         previous = nums[i]
        #         for j in range(i,len(nums)-1):
        #             nums[j] = nums[j+1]
        #         nums[-1] = previous
        ## This code doesn't work for any continus 0 like [0,0,1,12,3] or [1,0,0,12,3], it work for [1,0,12,3,0] which 0 is seperate. How to fix it?
        
        #Optimal solution, O(n) time, O(1) space
        # use two pointer, one is position(for zero element), another one is element( for nonzero element)
        position = 0
        for i in range(len(nums)):
            element = nums[i]
            if element != 0:
                # when first element is non-zero, swap with itself so no change, then position point to next element , which will always be the first zero idx
                nums[position], nums[i] = nums[i], nums[position]
                #swap the first non-zero value with the first zero 
                position += 1 
        
        
#  Q2: Two sum
                  
class Solution:
    # O(n) time | O(1) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] < target:
                left +=1
            else:
                right -=1
        # no solution case 
        retun (-1,-1)
                
        
        
        
