class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # this is equal to having two subsets one with negative signed ones and other with positive ones, we need the minus of these sum of subsets equal to target.
        
        def recur(i,temp_sum):
            if(i==len(nums)):
                if(temp_sum==target):
                    return 1
                else:
                    return 0
            if((i,temp_sum) in cache):
                return cache[(i,temp_sum)]
            p1 = recur(i+1,temp_sum+nums[i])
            p2 = recur(i+1,temp_sum-nums[i])
            res = p1+p2
            cache[(i,temp_sum)] = res
            return res
        
        cache = dict()
        return recur(0,0)
                
        
        
#         def recur(i,tar):
            
#             if(i==0):
#                 if(tar==0 and nums[i]==0):
#                     return 2
#                 if(tar==0 or tar-nums[i]==0):
#                     return 1
#                 return 0
#             if((i,tar) in cache):
#                 return cache[(i,tar)]
#             notTake = recur(i-1,tar)
#             take = 0
#             if(nums[i]<=tar):
#                 take = recur(i-1,tar-nums[i])
#             res = take+notTake
#             cache[(i,tar)] = res 
#             return res
        
#         total_sum = sum(nums)
#         new_target = (total_sum+target)/2
#         cache = dict()
#         # find number of subsets with sum=new_target
#         return recur(len(nums)-1,new_target)
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         tot = sum(nums)
#         n= len(nums)
#         if((tot+target)%2!=0 or tot<target ):
#             return 0
#         s=(tot+target)//2
#         if(s<0):
#             return 0
        
#         dp=[[0]*(s+1) for i in range(n+1)]
        
#         for i in range(n+1):
#             dp[i][0]=1
#         for j in range(1,s+1):
#             dp[0][j]=0
            
#         for i in range(1,n+1):
#             for j in range(0,s+1):
#                 if(nums[i-1]<=j):
#                     dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         return dp[n][s]