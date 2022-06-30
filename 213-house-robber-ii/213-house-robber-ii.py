class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        def hrob(nums):
            prev1 = 0
            prev2 = 0
            
            for n in nums:
                newrob = max(prev1+n, prev2)
                prev1 = prev2
                prev2 = newrob
                
            return prev2
        
        if(len(nums)==1):
            return nums[0]
        return max(hrob(nums[1:]), hrob(nums[:-1]))