class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0]*n
        res = 0
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]=="0"):
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + int(matrix[i][j])
            res = max(res, self.largestRectangleArea(dp))
        return res
                
        
        
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## Watch video https://www.youtube.com/watch?v=jC_cWLy7jSI&t=34s
        st = []
        st.append(0)
        n = len(heights)
        res = 0
        for i in range(1,n):
            rs = i-1
            while(len(st)>0 and heights[st[-1]]>=heights[i]):
                pop = st.pop()
                ls = 0
                if(len(st)>0):
                    ls = st[-1]+1
                area = (rs-ls+1)*heights[pop]
                res = max(area,res)
            st.append(i)
            
        rs = n-1
        while(len(st)>0):
            pop = st.pop()
            ls = 0
            if(len(st)>0):
                ls = st[-1]+1
            area = (rs-ls+1)*heights[pop]
            res = max(area,res)
        return res