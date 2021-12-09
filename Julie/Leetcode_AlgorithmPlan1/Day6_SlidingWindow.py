# Method 1: Naive
# class Solution:
#     # O(n^3) time: two "for" loop and check function inside which is O(n)
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # help function 
#         def check(start, end):
#             chars = [0]*128 #why 128? overall 128 character cases
#             for i in range(start, end+1):
#                 c = s[i] # loop the string charaters one by one
#                 chars[ord(c)] +=1 #ord() change char to int, mark the                                      repeated times for current charater
#                 if chars[ord(c)] > 1: 
#                     return False
#             return True # return true if all characters are unique in the substring 

#         n = len(s)

#         res = 0
#         for i in range(n):
#             for j in range(i,n): 
#                 if check(i,j): #O(n), check every substring 
#                     res = max(res, j-i+1) #why j-i+1? the current length for the substring 
#         return res
    

    
# Method 2: sliding window
# In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary. If a substring s_{ij}from index i to j - 1 is already checked to have no duplicate characters. We only need to check if s[j]s[j] is already in the substring s_{ij}
# To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2) algorithm. But we can do better.
# By using HashSet as a sliding window, checking if a character in the current can be done in O(1)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         chars = [0]*128
#         left = right = 0 # initial all point the first element
#         res = 0 # record result of longest no repeating substring
        
#         while right <len(s):
#             rs = s[right]
#             chars[ord(rs)] += 1 
            
#             # print(chars)
#             while chars[ord(rs)] > 1:
#                 ls = s[left]
#                 chars[ord(ls)] -= 1 # why? To contract the window by reduce the currence of left boundary, so it won't be included in the window
#                 left += 1 #left pointer is used to contract the window to the non repeated 
                
#             res = max(res, right - left +1)
            
#             right+=1 # right pointer is used to expand the window
            
#         return res



# A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i, j)[i,j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i, j) to the right by 11 element, then it becomes [i+1, j+1)(left-closed, right-open). The size of sliding window can be changed
  
# Method 3: Sliding window optimized, use hash map
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

