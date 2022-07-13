class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if(not heights):
            return None
        rows = len(heights)
        cols = len(heights[0])
        pacific =set()
        arctic =set()
        
        def dfs(i,j,visited,prevHeight):
            if((i,j) in visited or not isValid(i,j) or heights[i][j]<prevHeight):
                return 
            visited.add((i,j))
            dfs(i+1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
        
        def isValid(i,j):
            if(i<0 or i>=rows or j<0 or j>=cols):
                return False
            return True
        
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,arctic,heights[rows-1][c])
        
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,arctic,heights[r][cols-1])
        
        
        pacific = pacific.intersection(arctic)
        res = []
        for x in pacific:
            res.append(list(x))
        return res
        
        
        
        
#         #### Algorithms made easy utube vidoe approach
        
#         m=len(heights)
#         n=len(heights[0])
#         if(heights==None):
#             return None
#         res=[]
#         ## pacific arrat denotes whethe it is possible to reach pacific ocean from a particular cell in the matric, same goes with arctic
#         # pacific = [[False]*n]*m
#         pacific = [[False]*(n) for _ in range(m)]
#         arctic = [[False]*(n) for _ in range(m)]
        
#         prev=-1*(math.inf)
#         for i in range(m):
#             self.dfs(heights,i,0,prev,pacific)
#             self.dfs(heights,i,n-1,prev,arctic)
#         for j in range(n):
#             self.dfs(heights,0,j,prev,pacific)
#             self.dfs(heights,m-1,j,prev,arctic)
        
#         for i in range(m):
#             for j in range(n):
#                 if(pacific[i][j] and arctic[i][j]):
#                     res.append([i,j])
#         return res

#     def dfs(self,heights,i,j,prev,ocean):
#         if(i<0 or i>=len(ocean) or j<0 or j>=len(ocean[0])):
#             return   
        
#         if(heights[i][j]<prev or ocean[i][j]):
#             return
#         ocean[i][j]=True
        
#         self.dfs(heights,i,j+1,heights[i][j],ocean)
#         self.dfs(heights,i,j-1,heights[i][j],ocean)
#         self.dfs(heights,i+1,j,heights[i][j],ocean)
#         self.dfs(heights,i-1,j,heights[i][j],ocean)
        
        
                    