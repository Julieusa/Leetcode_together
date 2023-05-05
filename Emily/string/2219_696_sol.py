#an stupid solution
#ideas: count how many 0 and 1 groups and add them up, i.e. '0011000'->[2,2,3]->ans=0+min(2,2)+min(2,3)

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack_s=[]
        zeros,ones=0,0
        for i in range(len(s)):
            if i!=len(s)-1:
                if s[i]=='0' and s[i+1]=='0':
                    zeros=zeros+1
                elif s[i]=='0' and s[i+1]=='1':
                    zeros=zeros+1
                    stack_s.append(zeros)
                    zeros=0
                elif s[i]=='1' and s[i+1]=='1':
                    ones=ones+1
                else:
                    ones=ones+1
                    stack_s.append(ones)
                    ones=0
            else:
                if zeros==0 and ones==0:
                    stack_s.append(1)
                else:
                    stack_s.append(max(ones,zeros)+1)
            #print(stack_s)
        ans=0
        #print(stack_s)
        for j in range(len(stack_s)-1):
            ans=ans+min(stack_s[j],stack_s[j+1])
            #print(ans)
        return ans
                    
  #a short version
  class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans,prev,same=0,0,1
        for i in range(1,len(s)):
            if s[i-1]!=s[i]:
                ans=ans+min(prev,same)
                prev=same
                same=1
            else:
                same=same+1
        ans=ans+min(prev,same)
        return ans

        
