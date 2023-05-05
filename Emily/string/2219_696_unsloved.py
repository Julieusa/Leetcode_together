#correct for the first few iteration, then messed up with long query
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range (len(s)-1):
            count=self.find_count(count,s[i:])
        return count
    
    def find_count(self,count,s2):
        stack_s=[]
        for i in range(len(s2)):
            if not stack_s:
                stack_s.append(s2[i])
            else:
                if s2[i]==stack_s[-1]:
                    stack_s.append(s2[i])
                else:
                    stack_s.pop()
                    if not stack_s:
                        break
        
        if not stack_s:
            count=count+1
        return count
