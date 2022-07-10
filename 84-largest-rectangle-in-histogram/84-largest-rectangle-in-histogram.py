class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        st.append(0)
        n = len(heights)
        res = 0
        leftSmaller = [0]*n
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
            
                
            
                
                
        
        
        
        
        
#         # Two pass solution
#         # using monotonic stack to find the first left smaller element for every element in the array
#         # this stack stores indices
#         n = len(heights)
#         leftSmaller = [0]*n
#         st = []
#         # the left smaller of left most element will be itself hence we append 0
#         st.append(0)
#         for i in range(1,n):
#             while(len(st)>0 and heights[st[-1]]>=heights[i]):
#                 st.pop()
#             if(len(st)==0):
#                 leftSmaller[i] = 0
#                 st.append(i)
                
#             else:
#                 leftSmaller[i] = st[-1]+1
#                 st.append(i)

#         rightSmaller = [0]*n
#         rightSmaller[n-1] = n-1
#         st = []
#         # the right smaller of right most element will be itself hence we append index n-1
#         st.append(n-1)
#         for i in range(n-2,-1,-1):
#             while(len(st)>0 and heights[st[-1]]>=heights[i]):
#                 st.pop()
#             if(len(st)==0):
#                 rightSmaller[i] = n-1
#                 st.append(i)
                
#             else:
#                 rightSmaller[i] = st[-1]-1
#                 st.append(i)
                
        
#         # Now we can compute the max area
#         res = 0
#         for i in range(n):
#             area = heights[i]*(rightSmaller[i]-leftSmaller[i]+1)
#             res = max(res,area)
#         return res
            