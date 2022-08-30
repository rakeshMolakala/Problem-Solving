import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # first approach using heaps
        track = collections.defaultdict(int)
        for num in nums:
            track[num]+=1
        
        heap = []
        for key,value in track.items():
            heap.append((-value,key))
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            value,key = heapq.heappop(heap)
            res.append(key)
        return res
            
       
        # Second approach usign Bucket sort technique - O(n) solution
#         if(k==len(nums)):
#             return nums
#         track=dict()
#         for x in nums:
#             if x in track:
#                 track[x]=track[x]+1
#             else:
#                 track[x]=1
#         print(track)

#         res=[None]*(len(nums)+1)
#         values_keys = zip(track.values(), track.keys())
#         print(values_keys)
#         for v,key in values_keys:
#             print(v,key)
#             temp=[]
#             if(res[v]==None):
#                 res[v]=[key]
#             else:
#                 temp=[key]
#                 res[v]=res[v] + temp
#         ans=[]
#         print(res)
#         for i in range(len(nums),-1,-1):
#             if len(ans)<k and res[i]!=None:
#                 ans=ans+res[i]
#         return ans
                
            
        