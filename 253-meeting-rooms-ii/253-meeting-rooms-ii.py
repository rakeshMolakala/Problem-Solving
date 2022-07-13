import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        for x in intervals:
            starts.append(x[0])
            ends.append(x[1])
        starts.sort()
        ends.sort()
        
        s,e = 0,0
        res = 0
        count = 0
        while(s<len(intervals)):
            if(starts[s]<ends[e]):
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res = max(res,count)
        return res
                
        
        
        
        
        
        
        
        
        
#         intervals.sort()
#         prev = []
#         prev.append(intervals[0][1])
#         res=1
#         heapq.heapify(prev)
        
#         for i in range(1,len(intervals)):
#             roomFound = False
#             mini = prev[0]
#             if(intervals[i][0]>=mini):
#                 roomFound = True
#                 heapq.heappop(prev)
#                 heapq.heappush(prev,intervals[i][1])
#             else:
#                 res = res+1
#                 heapq.heappush(prev,intervals[i][1])
    
#         return res
    
    
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         intervals.sort()
#         prev = dict()
#         prev[0] = intervals[0][1]
#         res=1
#         for i in range(1,len(intervals)):
#             roomFound = False
#             for j,k in prev.items():
#                 if(intervals[i][0]>=k):
#                     roomFound = True
#                     prev[j]=intervals[i][1]
#                     break
#             if(not roomFound):
#                 res = res+1
#                 prev[i]=intervals[i][1]
#         return res