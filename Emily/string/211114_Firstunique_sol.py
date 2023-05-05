class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #counts=collections.Counter(s)
        #print(dict_)
        counts={}
        for num in s:
            counts[num] = counts.get(num, 0) + 1
        print(counts)
        for loc,item in enumerate(s):
            if counts[item]==1:
                return loc
        return -1
            
        #collection.Counters does the same thing as A.get(x,0)+1 for string
        #use the dict to find location and keep the orders.
