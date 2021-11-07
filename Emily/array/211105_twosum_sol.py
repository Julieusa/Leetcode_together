class Solution(object):
    def twoSum(self, nums, target):
        complements = {}
    
        for index, item in enumerate(nums):
            if item in complements: 
                return [complements[item], index]
            else:
                complements[target - item] = index
                
# This use the enumerate function, if nums=[2,7,11,15], then enumerate(nums)=[(0,2),(1,7),(2,11),(3,15)]
# by defining complements as dictory, it allow the appent not happened from 0 position.
#complements[9-2]=0, and complements={7:0}, if item=7, return[0,1(index of 7 in enumate)].

#Review enumerate():
#enumerate(iterable, start=0)

#Parameters:
#Iterable: any object that supports iteration
#Start: the index value from which the counter is 
#              to be started, by default it is 0

#e.g.: >s1 = "geek" >print (list(enumerate(s1,2)))
#[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
