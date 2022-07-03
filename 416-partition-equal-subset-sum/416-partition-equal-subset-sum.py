class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        def recur(i,summ):
            if(summ==target):
                return True;
            if(i==len(nums) or summ>target):
                return False
            if(cache[i][summ]!=None):
                return cache[i][summ]
            
            p1 = recur(i+1,summ)
            p2 = recur(i+1,summ+nums[i])
            res = p1 or p2
            
            cache[i][summ] = res 
            return res
        
        total_sum = sum(nums)
        if(total_sum%2!=0):
            return False
        target = total_sum//2
        cache = [[None]*(target+1) for _ in range(len(nums)+1)]
        return recur(0,0)
        
        
        
        
        
        
#         s = sum(nums)
#         n= len(nums)
#         if(s%2!=0):
#             return False;
#         s=s//2
#         dp=[[False]*(s+1) for i in range(n+1)]
#         dp[0][0]=True
        
#         for i in range(n+1):
#             dp[i][0]=True
#         for i in range(1,n+1):
#             for j in range(1,s+1):
#                 if(nums[i-1]<=j):
#                     dp[i][j] = (dp[i-1][j-nums[i-1]]) or (dp[i-1][j])
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         # print(dp)
#         return dp[n][s]
        