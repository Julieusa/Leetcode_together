#191 Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n:
            if n & 1: #same as n%1==1
                count+=1
            #print(n)
            #>> means for bits, everything except the first digit move to the next pos
            #and insert 0 at initial i.e., 0001101->0000110
            #do not use else bc shift is necessary
            n=n>>1
            #print(n)
        return count
      
 #338  Counting Bits
#don't need to transfer int to bits
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        new_list=[]
        for i in range(n+1):
            count=self.count_bits(i)
            new_list.append(count)
        return new_list
    
    def count_bits(self,n):
        count=0
        while n:
            if n&1:
                count=count+1
                
            n=n>>1
        return count
      
#sol:
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[0]*(n+1)
        for i in range(1,n+1):
            ans[i]=ans[i>>1]+(i&1) #(x&1 means check the last significant digit is equal to 1 or not, if yes->1, no ->0)
            
        return ans
