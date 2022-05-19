from collections import defaultdict

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        track = set()
        track2 = defaultdict(int)
        res = 0
        m= len(matrix)
        n = len(matrix[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        
        def dfs(i,j):
            track.add((i,j))
            if(track2[(i,j)]!=0):
                return track2[(i,j)]
            else:
                for x,y in directions:
                    tempx = x+i
                    tempy = y+j
                    if(tempx >= 0 and tempx<m and tempy>=0 and tempy<n and matrix[tempx][tempy]>matrix[i][j]):
                        track2[(i,j)] = max(track2[(i,j)],1+dfs(tempx,tempy))
                return track2[(i,j)]
                        
        
        for i in range(m):
            for j in range(n):
                if((i,j) not in track):
                    res = max(res,dfs(i,j))
        
        return res+1
                    
                    
                    
        
            