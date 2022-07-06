class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        # lets write code for Longest common subsequence
        m = len(str1)
        n = len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(str1[i-1]==str2[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        
        
        
        res=""
        while(m>0 and n>0):
            # if(m>0 and n<=0):
            #     res = str1[:m+1]+res
            #     continue
            # if(n>0 and m<=0):
            #     res = str1[:n+1]+res
            if(str1[m-1]==str2[n-1]):
                res = str1[m-1]+res
                m-=1
                n-=1
            elif(dp[m-1][n]>dp[m][n-1]):
                m=m-1
            else:
                n=n-1
        
        i, j, k = [0, 0, 0]
        ans = ""
        while i < len(res) and j < len(str1) and k < len(str2):
            if res[i] == str1[j] and res[i] == str2[k]:
                ans += res[i]
                i+=1
                j+=1
                k+=1
            elif res[i] == str1[j]:
                ans += str2[k]
                k+=1
            elif res[i] == str2[k]:
                ans += str1[j]
                j+=1
            else:
                ans += str1[j] + str2[k]
                j += 1
                k += 1
        while i < len(res):
            ans += res[i]
            i+=1
        while j < len(str1):
            ans += str1[j]
            j+=1
        while k < len(str2):
            ans += str2[k]
            k+=1
        return ans