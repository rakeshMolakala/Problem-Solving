import heapq
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        
        for i in range(len(nums)):            
            while(len(heap)>0 and nums[i]>heap[0][0]+1):
                last, length = heapq.heappop(heap)
                if(length<3):
                    return False
                
            
            if(len(heap)==0 or nums[i]==heap[0][0]):
                heapq.heappush(heap,(nums[i],1))
                
            if(nums[i]==heap[0][0]+1):
                length = heap[0][1]
                heapq.heappop(heap)
                heapq.heappush(heap,(nums[i],length+1))
    
                
        for sub in heap:
            if(sub[1]<3):
                return False
        
        return True
                
            
                
                
            
            
                
            
            
        