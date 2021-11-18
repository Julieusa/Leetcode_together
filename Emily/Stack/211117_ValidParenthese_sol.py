class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        open_b=['(','{','[']
        close_b=[')','}',']']
        for i in s:
            if i in open_b:
                stack.append(i)
            else:
                if stack and stack[-1]==open_b[close_b.index(i)]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
      
      #use pop, if dismatch then pop the last one out
