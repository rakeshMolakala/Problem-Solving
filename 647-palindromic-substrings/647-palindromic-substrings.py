class Solution:
    def countSubstrings(self, s: str) -> int:        
        n = len(s)
        res = 0
                    
        dp=[[False]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                ## for len(s) == 1
                if(i==j):
                    dp[i][j] = True
                    res+=1
                    
                ## for len(s) == 2
                elif(j-i==1):
                    if(s[i]==s[j]):
                        dp[i][j] = True
                        res+=1
                    else:
                        dp[i][j] = False
                
                ## for len(s)>2
                else:
                    if(dp[i+1][j-1] and s[i]==s[j]):
                        dp[i][j] = True
                        res+=1
                    else:
                        dp[i][j] = False
        return res
                    
                