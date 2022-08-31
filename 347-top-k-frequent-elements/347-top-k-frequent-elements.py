import heapq
class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         # first approach using heaps
#         track = collections.defaultdict(int)
#         for num in nums:
#             track[num]+=1
        
#         heap = []
#         for key,value in track.items():
#             heap.append((-value,key))
#         heapq.heapify(heap)
        
#         res = []
#         for i in range(k):
#             value,key = heapq.heappop(heap)
#             res.append(key)
#         return res
            
        
    # second approach using bucket sort - O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # first approach using heaps
        track = collections.defaultdict(int)
        for num in nums:
            track[num]+=1
            
        n = len(nums)
        temp = [[] for _ in range(n+1)]
        for key,val in track.items():
            temp[val].append(key)
        
        res = []
        for i in range(n,0,-1):
            for ele in temp[i]:
                if k==0:
                    return res
                res.append(ele)
                k-=1
        return res
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        