class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0]) #lambda x:small fun  alaways sort!!!!!
        for i in range(len(intervals)-1):
            low_a=intervals[i][0]
            high_a=intervals[i][1]
            low_b=intervals[i+1][0]
            high_b=intervals[i+1][1]
            if low_a<=low_b<=high_a or low_b<=low_a<=high_b:
                new_a=[min(low_a,low_b),max(high_a,high_b)]
                intervals[i+1]=new_a
                intervals[i]=[]
        rest=[j for j in intervals if j!=[]]
        return rest
                
