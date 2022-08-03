import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                res.append(matrix[i][j])
        
        ans = None
        heapq.heapify(res)
        while(k>0):
            ans = heapq.heappop(res)
            k-=1
        return ans
        