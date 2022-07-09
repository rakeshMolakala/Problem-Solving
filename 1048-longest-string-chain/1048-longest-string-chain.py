class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPred(s1,s2):
            p1 = len(s1)-1
            p2 = len(s2)-1
            oneViolation = False
            if(p2-p1!=1):
                return False
            while(p1>=0 or p2>=0):
                if(p1>=0 and s2[p2]==s1[p1]):
                    p1=p1-1
                    p2=p2-1
                else:
                    if(oneViolation):
                        return False
                    p2=p2-1
                    oneViolation = True
            if(p1==-1 and p2==-1):
                return True
            return False
            
        words = sorted(words,key=len)
        n = len(words)
        dp = [1]*n
        ans = 1
        for i in range(1,n):
            for j in range(i):
                if(isPred(words[j],words[i]) and dp[i]<dp[j]+1):
                    dp[i] = dp[j] + 1
            ans = max(ans,dp[i])
            
    
        return ans
        
        
        
        
                
            
            
                     
                     
                     
                                 
            
                     