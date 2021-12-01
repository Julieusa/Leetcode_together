class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map={}
        for loc,num in enumerate(order):
            order_map[num]=loc
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j>=len(words[i+1]):
                    return False
                if words[i][j]!=words[i+1][j]:
                    if order_map[words[i][j]]>order_map[words[i+1][j]]:
                        return False
                    break

                
        return True
