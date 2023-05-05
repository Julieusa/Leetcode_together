class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """        
        dict_m=collections.Counter(magazine)
        dict_r=collections.Counter(ransomNote)
        
        i=0
        while i<len(dict_r.keys()):
            keys_=dict_r.keys()[i]

            if dict_r[keys_]<=dict_m[keys_]:
                i+=1
            else:
                return False
            if i==len(dict_r.keys()):
                return True
              
              
              
              
              #sol:
              #return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))
              #A.count(c), return how many c is appeared in A.
