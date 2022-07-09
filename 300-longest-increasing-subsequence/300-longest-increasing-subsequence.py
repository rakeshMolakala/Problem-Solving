class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
        
#         def recur(i,prev):
#             if(i==n):
#                 return 0
#             if(dp[i][prev+1]!=-1 ):
#                 return dp[i][prev+1]
#             p1 = 0
#             if(prev==-1 or nums[prev]<nums[i]):
#                 p1 = 1 + recur(i+1,i)
#             p2 = 0 + recur(i+1,prev)
#             res = max(p1,p2)
#             dp[i][prev+1] = res
#             return res
            
#         dp = [[-1]*(n+1) for _ in range(n)]
#         return recur(0,-1)
        
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
                            
        ans = 0
        for i in range(n-1,-1,-1):
            for j in range(i-1,-2,-1):
                p1 = 0
                if(j==-1 or nums[j]<nums[i]):
                    p1 = 1 + dp[i+1][i+1]
                p2 = dp[i+1][j+1]
                res = max(p1,p2)
                dp[i][j+1] = res
        return dp[0][-1+1]
                
        
    
        
