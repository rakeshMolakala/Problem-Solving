class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        left = 0
        right = 0
        for i in range(numRows):
            cols = i+1
            temp = [0]*(cols)
            temp[0],temp[-1] = 1,1
            for j in range(1,cols-1):
                first = res[i-1][j-1]
                second = res[i-1][j]
                temp[j] = first+second
            res.append(temp)
                
        return res
                
                
        