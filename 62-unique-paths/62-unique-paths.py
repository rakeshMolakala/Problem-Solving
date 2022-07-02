class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def recur(row,col):
            if((row,col) in cache):
                return cache[(row,col)]
            
            if(row>=m or col>=n):
                return 0
            if(row==m-1 and col==n-1):
                return 1
            
            p1 = recur(row+1,col)
            p2 = recur(row,col+1)
            res = p1+p2
            cache[(row,col)] = res
            return res
        
        cache = dict()
        return recur(0,0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        