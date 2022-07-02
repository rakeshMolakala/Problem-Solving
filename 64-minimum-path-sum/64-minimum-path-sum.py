class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[None]*n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if(i==0 and j==0):
                    dp[i][j] = grid[0][0]
                    continue
                up = grid[i][j]
                left = grid[i][j]
                if(i>0):
                    up = up + dp[i-1][j]
                else:
                    up = up + dp[i][j-1]
                if(j>0):
                    left = left + dp[i][j-1]
                else:
                    left = left + dp[i-1][j]
                dp[i][j] = min(up,left)
        
        print(dp)
        return dp[m-1][n-1]
                
        
        
#         Top down approach

#         def recur(row,col):
#             if(row==m-1 and col==n-1):
#                 return grid[row][col]
            
#             if((row,col) in cache):
#                 return cache[(row,col)]
             
#             p1=math.inf
#             p2=math.inf
#             if(row+1<m): 
#                 p1 = grid[row][col] + recur(row+1,col)
#             if(col+1<n):
#                 p2 = grid[row][col] + recur(row,col+1)
            
#             res = min(p1,p2)
#             cache[(row,col)] = res
#             return res
            
#         cache = dict()
#         m=len(grid)
#         n=len(grid[0])
#         return recur(0,0)