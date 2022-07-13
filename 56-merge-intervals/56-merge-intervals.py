class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        if(len(intervals)==1):
            return intervals
        res = []
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if(res[-1][1]<intervals[i][0]):
                res.append(intervals[i])
            else:
                tempInterval = [res[-1][0],max(intervals[i][1],res[-1][1])]
                res.pop()
                res.append(tempInterval)
        return res
                
        