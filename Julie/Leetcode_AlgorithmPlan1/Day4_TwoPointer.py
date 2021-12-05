# Q1: Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # O(n) time | O(1) space
        left=0
        right = len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
     
    
# Q2: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
class Solution:
    # O(n) space O(n) time 
    def reverseWords_help(self, sub: str):
        
        # while left <= right:
        #     print([sub[left],sub[right-1]])
        #     # sub[left], sub[right-1] = sub[right-1], sub[left]
        #     # Error: 'str' object does not support item assignment
        #     left+=1
        #     right-=1
        subinv =""
        subinv= sub[::-1]
        return subinv
    
    def reverseWords(self, s: str) -> str:
        s=s+ " " #when using if, the last word can't be reversed so need a space in the end
        previous = 0
        result = ""
        for i in range(0,len(s)):
            # how to see space in python
            if s[i]== " ":
              subinv = self.reverseWords_help(s[previous: i])
              previous = i+1    
              result += subinv + " "
        result = result[0:len(result)-1]  #delete the space in the end
        return result
