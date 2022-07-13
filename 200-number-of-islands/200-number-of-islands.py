class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        rows, cols = len(grid),len(grid[0])
        islands = 0
        visited = set()
        
        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            while(q):
                r,c = q.pop()
                direc = [[0,1],[1,0],[-1,0],[0,-1]]
                for x,y in direc:
                    tr = r+x
                    tc = c+y
                    if(checkValidij(tr,tc) and (tr,tc) not in visited and grid[tr][tc]=='1'):
                        q.append((tr,tc))
                        visited.add((tr,tc))    
                
        def checkValidij(i,j):
            if(i<0 or i>=rows or j<0 or j>=cols):
                return False
            return True
                
            
        
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]=='1' and ((i,j) not in visited)):
                    bfs(i,j)
                    islands+=1
        
        return islands
                
            
        
        
        
        
        
        # dfs modifying the grid
#         if(not grid or len(grid)==0):
#             return 0
#         ans=0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if(grid[i][j]=="1"):
#                     ans=ans+self.dfs(grid,i,j)
#         return ans
    
    
#     def dfs(self,grid,i,j):
#         if(i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=="0"):
#             return 0
#         grid[i][j]="0"
#         self.dfs(grid,i-1,j)
#         self.dfs(grid,i+1,j)
#         self.dfs(grid,i,j-1)
#         self.dfs(grid,i,j+1)
#         return 1
                    