import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        track = collections.defaultdict(int)
        for x in arr:
            track[x] = track[x] + 1
        min_remove = len(arr)//2
        pq = []
        for k,v in track.items():
            pq.append(-v)
        res = 0
        heapq.heapify(pq)
        while(min_remove>0):
            val = heapq.heappop(pq)
            min_remove-=-val
            res+=1
        return res
        
        
        
            
        
        