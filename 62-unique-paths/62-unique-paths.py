class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # simple combinations approach
        down_moves = m-1
        right_moves = n-1
        total_moves = m+n-2
        # here we need to find the combinations of selecting either n-1 right moves from total moves or m-1 down moves from total moves, so we do this (total_moves)C(right_moves)
        
        
        numerator = 1
        denom = 1
        for i in range(total_moves-right_moves+1,total_moves+1):
            numerator = numerator*i
        for i in range(1,right_moves+1):
            denom = denom*i
        return numerator//denom
        
        
        
#         cache = dict()
        
#         def recur(i,j):
#             if i>=m or j>=n:
#                 return 0
#             if i==m-1 and j==n-1:
#                 return 1
#             if (i,j) in cache:
#                 return cache[(i,j)]                
#             down = recur(i+1,j)
#             right = recur(i,j+1)
#             res = down + right
#             cache[(i,j)] = res
#             return res
        
#         return recur(0,0)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Top down approach
#         def recur(row,col):
#             if((row,col) in cache):
#                 return cache[(row,col)]
            
#             if(row>=m or col>=n):
#                 return 0
#             if(row==m-1 and col==n-1):
#                 return 1
            
#             p1 = recur(row+1,col)
#             p2 = recur(row,col+1)
#             res = p1+p2
#             cache[(row,col)] = res
#             return res
        
#         cache = dict()
#         return recur(0,0)
        
        
        
        
        
#         Bottom up approach

#         dp=[[0]*n for i in range(m)]
#         dp[0][0] = 1
#         for i in range(1,m):
#             dp[i][0] = 1
#         for j in range(1,n):
#             dp[0][j] = 1
            
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
#         return dp[m-1][n-1]
        