class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # easy understadning dp bottom up solution
        # dp[i] represents the length of LIS that ends ith position, by including the ith element.
        n = len(nums)
        ans = 1
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if(nums[j]<nums[i]):
                    dp[i] = max(dp[i],1+dp[j])
            ans = max(ans,dp[i])
        return ans
        
        
        
        
        
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
        
        # bottom up
#         n = len(nums)
#         dp = [[0]*(n+1) for _ in range(n+1)]
                     
#         ans = 0
#         for i in range(n-1,-1,-1):
#             for j in range(i-1,-2,-1):
#                 p1 = 0
#                 if(j==-1 or nums[j]<nums[i]):
#                     p1 = 1 + dp[i+1][i+1]
#                 p2 = dp[i+1][j+1]
#                 res = max(p1,p2)
#                 dp[i][j+1] = res
#         return dp[0][-1+1]
    
        
        # space optimized
#         n = len(nums)
#         curr = [0]*(n+1)
#         nextt = [0]*(n+1)
                     
#         ans = 0
#         for i in range(n-1,-1,-1):
#             for j in range(i-1,-2,-1):
#                 p1 = 0
#                 if(j==-1 or nums[j]<nums[i]):
#                     p1 = 1 + nextt[i+1]
#                 p2 = nextt[j+1]
#                 res = max(p1,p2)
#                 curr[j+1] = res
#             nextt = curr.copy()
#         return nextt[-1+1]
    
    
        # easy understadning dp bottom up solution
        # dp[i] represents the length of LIS that ends ith position, by including the ith element.
        # n = len(nums)
        # dp = [1]*n
        # ans = 1
        # for i in range(1,n):
        #     for j in range(i):
        #         if(nums[i]>nums[j]):
        #             dp[i] = max(dp[i],dp[j]+1)
        #     ans = max(ans, dp[i])
        # return ans
        
        
        # printing LCS
#         n = len(nums)
#         dp = [1]*n
#         track = [0]*n
#         last_index = 0
#         ans = 1
#         for i in range(1,n):
#             track[i] = i
#             for j in range(i):
#                 if(nums[i]>nums[j] and dp[i]<dp[j]+1):
#                     dp[i] = dp[j]+1
#                     track[i] = j
                    
#             if(dp[i]>ans):
#                 ans = dp[i]
#                 last_index = i
            
#         res = []
#         prev_last_index = -1
#         while(True):
#             if(last_index==prev_last_index):
#                 break
#             res.append(nums[last_index])
#             prev_last_index = last_index
#             last_index = track[last_index]
#         res=res[::-1]
#         print(res)
        
#         return ans
                
        
    
        
