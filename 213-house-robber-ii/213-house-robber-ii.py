class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recur(i,arr,cache):
            if( i in cache):
                return cache[i]
            
            if(i>=len(arr)):
                return 0
            
            # refer LC 198 for house robber 1 solution and explanation
            p1 = arr[i] + recur(i+2,arr,cache)
            
            p2 = recur(i+1,arr,cache)
            
            res = max(p1,p2)
            cache[i] = res
            return res
        
        if(len(nums)==1):
            return nums[0]
        
        cache1 = dict()
        cache2 = dict()
        
        p3 = recur(0,nums[1:],cache1)
        p4 = recur(0,nums[:-1],cache2)
        
        return max(p3,p4)
        
        