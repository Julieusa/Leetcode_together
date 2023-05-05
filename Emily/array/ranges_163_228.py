#163
class Solution(object):
        
    def return_s(self,lower,upper):
        if lower==upper:
            return str(lower)
        elif lower<upper:
            return (str(lower)+"->"+str(upper))
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        output=[]
        if not nums:
            output.append(self.return_s(lower,upper))
            return output
        
        if nums[0]>lower:
            output.append(self.return_s(lower,nums[0]-1))
        if len(nums)==1:
            if nums[0]<upper:
                output.append(self.return_s(nums[0]+1,upper))
            return output
        else:
            previous_n=nums[0]        
            for i in range(1,len(nums)):
                num1=previous_n
                num2=nums[i]
                if num1+1<num2:
                    output.append(self.return_s(num1+1,num2-1))
                previous_n=num2

            if nums[-1]<upper:
                output.append(self.return_s(nums[-1]+1,upper))
            return output
          
   #another solution
      def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        output=[]
        pre=lower-1 #lower-1 not +1
        for i in range(len(nums)+1):
            if i<len(nums):
                curr=nums[i]
            else:
                curr=upper+1
            if pre+1<curr-1:
                output.append(str(pre+1)+"->"+str(curr-1))
            elif pre+1==curr-1:
                output.append(str(pre+1))
            pre=curr
        return output
      
      #228
      class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=0
        output=[]
        if not nums:
            return output
        pre=nums[0]
        for i in range(len(nums)):
            if i<len(nums)-1:
                if nums[i+1]-nums[i]!=1:
                    end=nums[i]
                    if pre!=end:
                        output.append(str(pre)+"->"+str(end))
                    else:
                        output.append(str(pre))
                    pre=nums[i+1]
            else:
                if pre==nums[-1]:
                    output.append(str(pre))
                else:
                    output.append(str(pre)+"->"+str(nums[-1])) #means last two are with diff 1
        return output
