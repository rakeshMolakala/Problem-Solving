class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=set()
        for i in range(n):
            for j in range(n):
                if(grid[i][j]==1):
                    self.dfs(grid,i,j,n,visited)
                    return self.bfs(grid,visited,n)
        
    def bfs(self,grid,visited,n):
        q=list(visited)
        dis=dict()
        for x in q:
            dis[(x)]=0
        direc=[[0,1],[1,0],[0,-1],[-1,0]]
        while(q):
            curr=q.pop(0)
            steps=dis[curr]
            for dr,dc in direc:
                    c=curr[0]+dr
                    d=curr[1]+dc
                    if(c>=0 and c<n and d>=0 and d<n and (c,d) not in visited):
                        q.append((c,d))
                        dis[(c,d)]=steps+1
                        visited.add((c,d))   
                        if(grid[c][d]==1):
                            return steps
        # res=0
        # q=list(visited)
        # direc=[[0,1],[1,0],[0,-1],[-1,0]]
        # while(q):
        #     for i in range(len(q)):
        #         curr=q.pop(0)
        #         for dr,dc in direc:
        #             c=curr[0]+dr
        #             d=curr[1]+dc
        #             if((c,d) in visited or c<0 or d<0 or c>n-1 or d>n-1):
        #                 continue
        #             if(grid[c][d]==1):
        #                 return res
        #             q.append((c,d))
        #             visited.add((c,d))
        #     res+=1
                    
    def dfs(self,grid,i,j,n,visited):
        if(i<0 or j<0 or i>n-1 or j>n-1 or (i,j) in visited or grid[i][j]==0):
            return 
        visited.add((i,j))
        self.dfs(grid,i,j+1,n,visited)
        self.dfs(grid,i+1,j,n,visited)
        self.dfs(grid,i,j-1,n,visited)
        self.dfs(grid,i-1,j,n,visited)