class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s=[]
        for i in s:
            if i=='(' or i==')':
                new_s.append(i)
        #print(new_s)
        stack_s=[]
        if len(new_s)==0:
            return 0
        
        count=0
        for j in new_s:
            if j=='(':
                stack_s.append(j)
            elif j==')' and stack_s:
                stack_s.pop()
            else:
                count=count+1
            #print(stack_s,count)
                
        return len(stack_s)+count
