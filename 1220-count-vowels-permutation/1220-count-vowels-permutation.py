class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        #Top down recursion approach
        dic = {"":['a','e','i','o','u'],'a':['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['u','i'],'u':['a']}
        cache = dict()
        cons = 1000000007
        
        def recur(prev,n):
            if((prev,n) in cache):
                return cache[(prev,n)]
            if(n==0):
                return 1
            temp_ans = 0
            lis = dic[prev]
            for c in lis:
                temp_ans = temp_ans + recur(c,n-1)
            temp_ans = temp_ans % cons
            cache[(prev,n)] = temp_ans
            return temp_ans
        
        return recur("",n)
    
        
#         # Bottom up approach
#         dic = {0:[1,2,3,4,5],1:[2],2:[1,3],3:[1,2,4,5],4:[3,5],5:[1]} 
#         cons = 1000000007
#         dp = [[0 for _ in range(n+1)] for _ in range(6)]
#         for i in range(0,6):
#             dp[i][0] = 1
#         for i in range(0,6):
#             for j in range(1,n+1):
#                 temp_ans = 0
#                 for c in dic[i]:
#                     dp[i][j] = dp[i][j] + dp[c][j-1]
#                 dp[i][j] = dp[i][j] % cons
#         print(dp)
#         return 4
                
        
        
        
        