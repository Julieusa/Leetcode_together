class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        else:
            if len(digits)==1:
                return [1,0]
            else:
                pointer=1
                while pointer<=len(digits):
                    if digits[-pointer-1]!=9:
                        digits[-pointer-1]+=1
                        digits[-pointer]=0
                        return digits
                    else:
                        digits[-pointer]=0
                        pointer+=1
                        
                    if pointer==len(digits):
                        array1=[0]*pointer
                        array2=[1]
                        return array2+array1
                      
                   #Runtime: 16 ms, faster than 91.95% of Python online submissions for Plus One.
#Memory Usage: 13.3 MB, less than 70.75% of Python online submissions for Plus One.
#need to reduce the number of lines
