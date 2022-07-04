class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        def recur(i,prevSlopePositive,cache):
            if(i>=len(nums)-1):
                return 1
            p1 = 0
            p2 = 0
            if(i in cache):
                return cache[i]
            if(prevSlopePositive):
                if(nums[i+1]<nums[i]):
                    p1 = 1 + recur(i+1,False,cache)
                else:
                    p1 = recur(i+1,True,cache)

            else:
                if(nums[i+1]<=nums[i]):
                    p2 = recur(i+1,False,cache)
                else:
                    p2 = 1 + recur(i+1,True,cache)
                    
                    
            cache[i] = max(p1,p2)
            return max(p1,p2)
                
        return max(recur(0,True,dict()),recur(0,False,dict()))