import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        track = collections.defaultdict(int)
        n = len(arr)
        for x in arr:
            track[x] = track[x] + 1
        min_remove = n//2
        pq = []
        for k,v in track.items():
            pq.append((-v,k))
        res = 0
        heapq.heapify(pq)
        while(min_remove>0):
            val,key = heapq.heappop(pq)
            min_remove-=-val
            res+=1
        return res
        
        
        
            
        
        