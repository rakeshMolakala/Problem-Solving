class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        ## recur(i) represents the maximum wealth possible from considering the house at index i
        
        def recur(i):
            if(i in cache):
                return cache[i]
            
            if(i>=len(nums)):
                return 0
            
            #possibility one, to inlcude the current house
            p1 = nums[i] + recur(i+2)
            
            # possibility two, to not include the current house
            p2 = recur(i+1)
            
            res = max(p1,p2)
            cache[i] = res
            return res
        
        cache = {}
        return recur(0)
        