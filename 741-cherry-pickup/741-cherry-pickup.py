class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        def recur(i1,j1,j2):
            if((i1,j1,j2) in cache):
                return cache[(i1,j1,j2)]
            i2 = i1+j1-j2
            # check boundary conditions
            if(i1==n or i2==n or j1==n or j2==n or grid[i1][j1]==-1 or grid[i2][j2]==-1):
                return -math.inf
            
            # check end state
            if(i1==i2 and j1==j2 and i1==n-1 and j1==n-1):
                return grid[n-1][n-1]
            
            res = grid[i1][j1]
            if (j1!=j2):
                res = res + grid[i2][j2]
            
            res = res + max(recur(i1+1,j1,j2),recur(i1+1,j1,j2+1),recur(i1,j1+1,j2),recur(i1,j1+1,j2+1))
            
            cache[(i1,j1,j2)] = res
            return res

        cache = dict()            
        n = len(grid)
        return max(0,recur(0,0,0))
        
        