class Solution:
    def maxProfit(self, l: int, prices: List[int]) -> int:
        # Top Down
#         n = len(prices)
#         def recur(i,buy,number):
#             # Base cases
#             if(number==k):
#                 return 0
#             if(i==n-1):
#                 if(buy):
#                     return 0
#                 else:
#                     return prices[i]
            
            
#             # using Cached result
#             if((i,buy,number) in cache):
#                 return cache[(i,buy,number)]
            
#             res = 0
#             if(buy):
#                 # will buy
#                 p1 = -prices[i] + recur(i+1,False,number)
#                 # not buy
#                 p2 = recur(i+1,True,number)
#                 res = max(p1,p2)
#             else:
#                 # will sell
#                 p1 = prices[i] + recur(i+1,True,number+1)
#                 # not sell
#                 p2 = recur(i+1,False,number)
#                 res = max(p1,p2)
            
#             cache[(i,buy,number)] = res
#             return res
        
#         cache = dict()
#         if(len(prices)==0):
#             return 0
#         return recur(0,True,0)   
    
    
        # Bottom up
#         n = len(prices)
#         if(n==0):
#             return 0
#         dp = [[[0 for _ in range(l+1)] for _ in range(2)] for _ in range(n)]
        
#         for j in range(2):
#             for k in range(l+1):
#                 # buy
#                 if j==1:
#                     dp[n-1][j][k] = 0
#                 # sell
#                 else:
#                     dp[n-1][j][k] = prices[n-1]
                    
#         for i in range(n):
#             for j in range(2):
#                 dp[i][j][l] = 0
                
#         for i in range(n-2,-1,-1):
#             for j in range(2):
#                 for k in range(l-1,-1,-1):
#                     if(j==1):
#                         p1 = -prices[i] + dp[i+1][0][k]
#                         p2 = dp[i+1][1][k]
#                         dp[i][j][k] = max(p1,p2)
#                     else:
#                         p1 = prices[i] + dp[i+1][1][k+1]
#                         p2 = dp[i+1][0][k]
#                         dp[i][j][k] = max(p1,p2)
                        
#         return dp[0][1][0]       

        # Space optimized
        n = len(prices)
        if(n==0):
            return 0
        nextt = [[0]*(l+1) for _ in range(2)]
        for j in range(2):
            for k in range(l+1):
                if(j==1):
                    nextt[j][k]=0
                else:
                    nextt[j][k]=prices[n-1]
        for j in range(2):
            nextt[j][l] = 0
        curr = [[0]*(l+1) for _ in range(2)]

        for i in range(n-2,-1,-1):
            for j in range(2):
                for k in range(l-1,-1,-1):
                    if(j==1):
                        p1 = -prices[i] + nextt[0][k]
                        p2 = nextt[1][k]
                        curr[j][k] = max(p1,p2)
                    else:
                        p1 = prices[i] + nextt[1][k+1]
                        p2 = nextt[0][k]
                        curr[j][k] = max(p1,p2)
            nextt = curr.copy()  
        return nextt[1][0]