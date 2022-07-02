# from collections import defaultdict
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def recur(row,col):
            if((row,col) in cache):
                return cache[(row,col)]
            if(row>=m or col>=n):
                return 0
            
            if(obstacleGrid[row][col]==1):
                return 0
            if(row==m-1 and col==n-1):
                return 1
            
            p1 = recur(row+1,col)
            p2 = recur(row,col+1)
            res = p1+p2
            cache[(row,col)] = res
            return res
        
        cache = dict()
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        return recur(0,0)
        
        
        
        
        
        
        
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         if(obstacleGrid[0][0]==1):
#             return 0
#         dp = [[0]*n for i in range(m)]
#         dp[0][0] = 1
#         for i in range(1,m):
#             if(obstacleGrid[i][0]==0 and dp[i-1][0]==1):
#                 dp[i][0] = 1
#         for j in range(1,n):
#             if(obstacleGrid[0][j]==0 and dp[0][j-1]==1):
#                 dp[0][j] = 1
        
#         for i in range(1,m):
#             for j in range(1,n):
#                 if(obstacleGrid[i][j]==1):
#                     dp[i][j] = 0
#                 else:
#                     dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
#         print(dp)
        
#         return dp[m-1][n-1]
        
        
                    
        