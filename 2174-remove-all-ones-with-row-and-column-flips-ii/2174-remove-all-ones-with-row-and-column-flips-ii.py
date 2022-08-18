class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        min_operations = math.inf
        m = len(grid)
        n = len(grid[0])
        
        curr_row = [0]*n
        curr_col = [0]*m
        
        for i in range(m):
            for j in range(n):
                
                if(grid[i][j]==0):
                    continue
                
                for col in range(n):
                    curr_row[col] = grid[i][col]
                    grid[i][col] = 0
                
                for row in range(m):
                    curr_col[row] = grid[row][j]
                    grid[row][j] = 0
                    
                min_operations = min(min_operations,1+self.removeOnes(grid))
                
                for row in range(m):
                    grid[row][j] = curr_col[row]
                    
                for col in range(n):
                    grid[i][col] = curr_row[col]
                
                
                    
        if min_operations==math.inf:
            return 0
        return min_operations
                    
                            