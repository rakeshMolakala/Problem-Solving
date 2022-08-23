class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(cols):
            for j in range(rows):
                res[i][j] = matrix[j][i]
        return res