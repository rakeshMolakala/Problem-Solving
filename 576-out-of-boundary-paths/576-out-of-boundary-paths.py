class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        direc = [[1,0],[0,1],[-1,0],[0,-1]]
        M = 1000000007
        
        def recur(i,j,moves):
            if(i<0 or i>=m or j<0 or j>=n):
                return 1
            if(moves==0):
                return 0
            if((i,j,moves) in cache):
                return cache[(i,j,moves)]
            res = 0
            for d in direc:
                curx = i+d[0]
                cury = j+d[1]
                res = res + recur(curx,cury,moves-1)%M
            res = res % M
            cache[(i,j,moves)] = res 
            return res
        
        cache = dict()
        return recur(startRow,startColumn,maxMove)
            
                
        