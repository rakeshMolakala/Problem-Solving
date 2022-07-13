class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expanding from middle 
        
        res =""
        res_len = 0
        
        for i in range(len(s)):
            # odd length palindromes
            l,r=i,i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>res_len):
                    res_len = r-l+1
                    res = s[l:r+1]
                l=l-1
                r=r+1
            
            
            #even length palindromes
            l,r=i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>res_len):
                    res_len = r-l+1
                    res = s[l:r+1]
                l=l-1
                r=r+1
        return res
                
        
        