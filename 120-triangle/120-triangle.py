class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        def recur(row,col):
            if((row,col) in cache):
                return cache[(row,col)]
            
            res = triangle[row][col]
            if(row+1<len(triangle)):
                p1 = res + recur(row+1,col)
                p2 = res + recur(row+1,col+1)
                res = min(p1,p2)
                
            cache[(row,col)] = res
            return res
          
        cache = dict()
        return recur(0,0)