class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        else:
            array=[0,1]
            for i in range (n-1):
                array.append(array[-1]+array[-2])
            return array[-1]
          
 #save memory         
 class Solution:
    def fib(self, N):
        if N<=1:
            return N
        a, b = 0, 1
    	for i in range(N): 
            a, b = b, a + b
    	return b
