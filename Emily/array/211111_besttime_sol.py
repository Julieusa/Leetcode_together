class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1:
            return 0
        else:
            profit=0
            i=0
            while i<len(prices)-1:
                if prices[i]<prices[i+1]:
                    buy=prices[i]
                    break
                else:
                    i=i+1
            if i==len(prices)-1:
                return 0
            else:
                for j in range(i,len(prices)):
                    if profit<prices[j]-buy:
                        profit=prices[j]-buy
                    if prices[j]<buy:
                        buy=prices[j]
                return profit
          
          #Leetcode dislike max/min and double for      
                    
                    
            """      
            for i in range(len(prices)-1):
                if prices[i]<prices[i+1]:
                    buy=prices[i]
                    array1.append(max(prices[i:])-buy)
                    #print(array1)
            return max(array1)
        """  
