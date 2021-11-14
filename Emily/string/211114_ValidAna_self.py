class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        else:
            return all(s.count(c)==t.count(c) for c in set(s))
          
        #use set() can improve speed because it screening the repreated letters
