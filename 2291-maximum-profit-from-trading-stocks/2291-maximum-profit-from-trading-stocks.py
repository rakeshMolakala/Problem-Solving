class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
#         n = len(present)
        
#         def recur(i,money):
#             if(i==n-1):
#                 if(money>=present[i] and future[i]-present[i]>0):
#                     return future[i]-present[i]
#                 else:
#                     return 0
        
#             if((i,money) in cache):
#                 return cache[(i,money)]
            
#             res = 0
#             # buy
#             p1 = 0
#             if(money>=present[i]):
#                 p1 = future[i] - present[i] + recur(i+1,money-present[i])
#             # not buy
#             p2 = recur(i+1,money)
#             res = max(0,p1,p2)
#             cache[(i,money)] = res
#             return res
            
#         cache = dict()
#         return max(0,recur(0,budget))
    
    
        n = len(present)
        dp = [[0]*(budget+1) for _ in range(n)]
        for j in range(budget+1):
            if(j>=present[n-1] and future[n-1]-present[n-1]>0):
                dp[n-1][j] = future[n-1]-present[n-1]
            else:
                dp[n-1][j] = 0
    
        for i in range(n-2,-1,-1):
            for j in range(budget+1):
                p1 = 0
                if(j>=present[i]):
                    p1 = future[i] - present[i] + dp[i+1][j-present[i]]
                p2 = dp[i+1][j]
                dp[i][j] = max(0,p1,p2)
        
        return dp[0][budget]
            

   