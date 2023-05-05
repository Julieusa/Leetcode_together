class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s=list(s)
        loc_s=[]
        for i, item in enumerate(s):
            if item =='(':
                loc_s.append(i)
            elif item ==')':
                if loc_s:
                    loc_s.pop()
                else:
                    s[i]=''
        #print(s,loc_s)
        while loc_s:
            s[loc_s.pop()]=''
        return ''.join(s)
