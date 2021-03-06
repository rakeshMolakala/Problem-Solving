class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Longest common substring
        # def lcs(str1, str2):
        #     m = len(str1)
        #     n = len(str2)
        #     dp = [[0]*(n+1) for _ in range(m+1)]
        #     res = 0
        #     for i in range(1,m+1):
        #         for j in range(1,n+1):
        #             if(str1[i-1]==str2[j-1]):
        #                 dp[i][j] = 1+dp[i-1][j-1]
        #             else:
        #                 dp[i][j] = 0
        #             res = max(res,dp[i][j])
        #     return res
        
#         # print Longest common subsequence
#         def recur(i1,i2):
#             if(i1<0 or i2<0):
#                 return ""
#             if((i1,i2) in cache):
#                 return cache[(i1,i2)]
#             if(text1[i1]==text2[i2]):
#                 res = recur(i1-1,i2-1)+text1[i1]
#                 cache[(i1,i2)] = res
#                 return res
#             p1 = recur(i1,i2-1)
#             p2 = recur(i1-1,i2)
#             res = ""            
#             if(len(p1)>len(p2)):
#                 res = p1
#             else:
#                 res = p2
#             cache[(i1,i2)] = res
#             return res
        
#         cache = dict()
#         print(recur(len(text1)-1,len(text2)-1))
#         return 3
        
        
        # Bottom up with space optimization
        # m= len(text1)
        # n = len(text2)
        # prev = [0]*(n+1)
        # curr = [0]*(n+1)
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if(text1[i-1]==text2[j-1]):
        #             curr[j] = 1 + prev[j-1]
        #         else:
        #             curr[j] = max(prev[j],curr[j-1])
        #     prev = curr.copy()
        # return prev[n]
        
        
        # Bottom up 
#         m= len(text1)
#         n = len(text2)
#         dp = [[0]*(n+1) for _ in range(m+1)]
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if(text1[i-1]==text2[j-1]):
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#         return dp[m][n]
           
    
        # Top down approach
        def recur(i1,i2,):
            if(i1<0 or i2<0):
                return 0
            if((i1,i2) in cache):
                return cache[(i1,i2)]
            if(text1[i1]==text2[i2]):
                cache[(i1,i2)] = 1+recur(i1-1,i2-1)
                return cache[(i1,i2)]
            p1 = recur(i1,i2-1)
            p2 = recur(i1-1,i2)
            cache[(i1,i2)] = max(p1,p2)
            return max(p1,p2)
        
        cache = dict()
        return recur(len(text1)-1,len(text2)-1)


    
    