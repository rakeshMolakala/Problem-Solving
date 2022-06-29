class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            curr = i+1
            temp = [0]*curr
            temp[0],temp[-1] = 1,1
            
            for j in range(1,curr-1):
                temp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(temp)
                
        return res
                
        