class Solution:
    def countSubstrings(self, s: str) -> int:        
#         n = len(s)
#         res = 0
                    
#         dp=[[False]*n for _ in range(n)]
        
#         for i in range(n-1,-1,-1):
#             for j in range(i,n):
#                 ## for len(s) == 1
#                 if(i==j):
#                     dp[i][j] = True
#                     res+=1
                    
#                 ## for len(s) == 2
#                 elif(j-i==1):
#                     if(s[i]==s[j]):
#                         dp[i][j] = True
#                         res+=1
#                     else:
#                         dp[i][j] = False
                
#                 ## for len(s)>2
#                 else:
#                     if(dp[i+1][j-1] and s[i]==s[j]):
#                         dp[i][j] = True
#                         res+=1
#                     else:
#                         dp[i][j] = False
#         return res
        
        #expanding from middle 
        
        res =""
        res_len = 0
        count = 0
        
        for i in range(len(s)):
            # odd length palindromes
            l,r=i,i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                count = count + 1
                # if(r-l+1>res_len):
                #     res_len = r-l+1
                #     res = s[l:r+1]
                l=l-1
                r=r+1
            
            #even length palindromes
            l,r=i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                count = count + 1
                # if(r-l+1>res_len):
                #     res_len = r-l+1
                #     res = s[l:r+1]
                l=l-1
                r=r+1
        return count
                    
                