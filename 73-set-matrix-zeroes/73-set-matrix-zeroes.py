class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return None
        r = len(matrix)
        c = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in rows:
            for j in range(c):
                matrix[i][j]=0
        
        for j in cols:
            for i in range(r):
                matrix[i][j]=0
            
            
        