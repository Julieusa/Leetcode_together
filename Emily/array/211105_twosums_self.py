class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    return [i,j]
                  
#Runtime: 3576 ms, faster than 25.73% of Python online submissions for Two Sum.
#Memory Usage: 14.3 MB, less than 48.96% of Python online submissions for Two Sum.


        diff=[]
        for i in range(len(nums)):
            diff.append(target-nums[i])
        
        comm=list(set(diff).intersection(nums))
                
        #return comm
        if len(comm)==2: 
            for j in range(len(nums)):
                if nums[j]==comm[0]:
                    loc1=j

            for k in range(len(nums)):
                if nums[k]==comm[1]:
                    loc2=k
            return [loc1,loc2]
        
        else: 
            if len(comm)==1:
                loc_list=list()
                for m in range(len(nums)):
                    if nums[m]==target/2:
                        loc_list.append(m)
                return loc_list
            else:
                comm.remove(target/2)
                for j in range(len(nums)):
                    if nums[j]==comm[0]:
                        loc1=j

                for k in range(len(nums)):
                    if nums[k]==comm[1]:
                        loc2=k
                return [loc1,loc2]
            
#Runtime: 52 ms, faster than 71.15% of Python online submissions for Two Sum.
#Memory Usage: 14.5 MB, less than 24.56% of Python online submissions for Two Sum.
