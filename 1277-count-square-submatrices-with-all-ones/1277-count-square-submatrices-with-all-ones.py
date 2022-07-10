class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            dp[i][0] = matrix[i][0]
            res = res + dp[i][0]
        for j in range(1,n):
            dp[0][j] = matrix[0][j]
            res = res+ dp[0][j]
        for i in range(1,m):
            for j in range(1,n):
                if(matrix[i][j]==1):
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                else:
                    dp[i][j] = 0
                res = res + dp[i][j]
        return res