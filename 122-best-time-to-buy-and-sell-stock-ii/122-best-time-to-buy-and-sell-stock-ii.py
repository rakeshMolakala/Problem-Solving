class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Top down
#         def recur(i,buy):
            
#             if(i==len(prices)-1):
#                 if(buy):
#                     return 0
#                 else:
#                     return prices[i]
                
#             if((i,buy) in cache):
#                 return cache[(i,buy)]
            
#             res = 0
#             ## Allowed to buy
#             if(buy):
#                 # buy
#                 p1 = -prices[i] + recur(i+1,False)
#                 # not buy
#                 p2 = recur(i+1,True)
#                 res = max(p1,p2)
#             ## Allowed to sell
#             else:
#                 # sell
#                 p1 = prices[i] + recur(i+1,True)
#                 # not sell
#                 p2 = recur(i+1,False)
#                 res = max(p1,p2)
                
#             cache[(i,buy)] = res
#             return res
               
#         cache = dict()
#         return recur(0,True) 
    
        # Bottom up
#         n = len(prices)
#         dp = [[0]*2 for _ in range(n)]
#         dp[n-1][1] = 0
#         dp[n-1][0] = prices[n-1]
        
#         for i in range(n-2,-1,-1):
#             for j in range(2):
#                 if(j==1):
#                     p1 = -prices[i] + dp[i+1][0]
#                     p2 = dp[i+1][1]
#                     dp[i][j] = max(p1,p2)
#                 else:
#                     p1 = prices[i] + dp[i+1][1]
#                     p2 = dp[i+1][0]
#                     dp[i][j] = max(p1,p2)
    
#         return dp[0][1]
    
        # Space optimized
        n = len(prices)
        
        nextt = [prices[n-1],0]
        curr = [None,None]
        
        for i in range(n-2,-1,-1):
            for j in range(2):
                if(j==1):
                    p1 = -prices[i] + nextt[0]
                    p2 = nextt[1]
                    curr[j] = max(p1,p2)
                else:
                    p1 = prices[i] + nextt[1]
                    p2 = nextt[0]
                    curr[j] = max(p1,p2)
                    
            nextt = curr.copy()
        return nextt[1]
        
        
        
        
        
        
        
        
        
        
        
        
        