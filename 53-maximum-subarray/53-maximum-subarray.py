class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[None]*len(nums)
        dp[0]=nums[0]
        res = dp[0]
        for i in range(1,len(nums)):
            if(dp[i-1]+nums[i]>nums[i]):
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]
            
            res = max(res,dp[i])
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # prevmax = -math.inf
        # currmax = 0
        # start = 0;
        # end =0;
        # for i in range(len(nums)):
        #     if(nums[i]<=currmax+nums[i]):
        #         currmax = currmax+nums[i]
        #     else:
        #         start =i
        #         currmax = nums[i]
        #     if(prevmax<currmax):
        #         prevmax = currmax
        #         end=i
        # return prevmax
        
        # dp = [-math.inf]*len(nums)
        # dp[0] = nums[0]
        # start = 0
        # end = 0
        # maxi = nums[0]
        # for i in range(1,len(nums)):
        #     if(nums[i]>dp[i-1]+nums[i]):
        #         dp[i] = nums[i]
        #         start = i
        #     else:
        #         dp[i] = dp[i-1]+nums[i]
        #     if(dp[i]>maxi):
        #         maxi=dp[i]
        #         end=i
        # print(dp)
        # return maxi
    
        
                
        