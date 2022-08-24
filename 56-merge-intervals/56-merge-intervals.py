class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort according to the start time
        intervals.sort(key = lambda x:x[0])
        n = len(intervals)
        if n<=1:
            return intervals
        res = []
        res.append(intervals[0])
        
        for i in range(1,n):
            prev_start, prev_end = res[-1][0], res[-1][1]
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if(prev_end<curr_start):
                res.append(intervals[i])
            else:
                new_interval = [prev_start,max(prev_end,curr_end)]
                res.pop()
                res.append(new_interval)
        return res
