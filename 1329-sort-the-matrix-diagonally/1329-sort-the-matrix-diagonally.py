import heapq
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        hmap = collections.defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                hmap[i-j].append(mat[i][j])
                
        for key,val in hmap.items():
            heapq.heapify(val)
            
        for i in range(rows):
            for j in range(cols):
                value = heapq.heappop(hmap[i-j])
                mat[i][j] = value
        
        return mat