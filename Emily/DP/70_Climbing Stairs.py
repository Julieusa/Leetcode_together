class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        else:
            array=[1,2]
            for i in range(n-2):
                array.append(array[-2]+array[-1])
            return array[-1]
            
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        else:
            a=1
            b=2
            #array=[1,2]
            for i in range(n-2):
                c=a+b
                a=b
                b=c
                #array.append(array[-2]+array[-1])
            return c
        
