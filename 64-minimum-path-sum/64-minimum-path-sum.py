class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def recur(row,col):
            if(row==m-1 and col==n-1):
                return grid[row][col]
            
            if((row,col) in cache):
                return cache[(row,col)]
            
            p1=math.inf
            p2=math.inf
            if(row+1<m): 
                p1 = grid[row][col] + recur(row+1,col)
            if(col+1<n):
                p2 = grid[row][col] + recur(row,col+1)
            
            res = min(p1,p2)
            cache[(row,col)] = res
            return res
            
        cache = dict()
        m=len(grid)
        n=len(grid[0])
        return recur(0,0)