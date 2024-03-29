class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
        
    def transpose(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        