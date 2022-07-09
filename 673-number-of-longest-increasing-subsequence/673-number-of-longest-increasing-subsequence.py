class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n
        count = [1]*n
        
        ans = 1
        for i in range(1,n):
            for j in range(i):
                if(nums[j]<nums[i] and dp[i]<dp[j]+1):
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif(nums[j]<nums[i] and dp[i]==dp[j]+1):
                    count[i] = count[i] + count[j] 

            ans = max(ans,dp[i])
        
        res = 0
        for i in range(n):
            if(dp[i]==ans):
                res+=count[i]
        return res
        