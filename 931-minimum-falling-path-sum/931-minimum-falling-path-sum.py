class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def recur(row,col):
            if((row,col) in cache):
                return cache[(row,col)]
            
            res = matrix[row][col]
            if(row+1<len(matrix)):
                p1 = res + recur(row+1,col)
                p2 = math.inf
                p3 = math.inf
                if(col-1>=0):
                    p2 = res + recur(row+1,col-1)
                if(col+1<len(matrix[0])):
                    p3 = res + recur(row+1,col+1)
                res = min(p1,p2,p3)
            cache[(row,col)] = res
            return res
        
        cache = dict()
        ans = math.inf
        for i in range(1):
            for j in range(len(matrix[0])):
                ans = min (ans, recur(i,j))
                
        return ans