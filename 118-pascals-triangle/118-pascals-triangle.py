class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        left = 0
        right = 0
        for i in range(1,numRows):
            temp = []
            cols = i+1
            for j in range(cols):
                first, second = 0, 0
                if(j>0):
                    first = res[i-1][j-1]
                if(j<cols-1):
                    second = res[i-1][j]
                temp.append(first+second)
            res.append(temp)
                
        return res
                
                
        