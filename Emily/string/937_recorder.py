937. Reorder Data in Log Files

1. self-solution:
  class Solution(object):
    def get_key(self,ele):
        ids,item=ele.split(" ",1)
        return (item,ids)
        
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        str_=[]
        nums=[]
        for i in logs:
            ids,item=i.split(" ",1)
            if item[0].isalpha(): # letter
                str_.append(i)
            else:
                nums.append(i)
        
        return sorted(str_,key=self.get_key)+nums
      
 2. clean solution:
  class Solution(object):
    def get_key(self,ele):
        ids,item=ele.split(" ",1)
        if item[0].isalpha():
            return (0,item,ids) # define three things at a time
        else:
            return (1,)
        
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        return sorted(logs,key=self.get_key)
