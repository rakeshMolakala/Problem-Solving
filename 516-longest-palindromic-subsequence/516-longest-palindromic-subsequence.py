class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        
        # t is the reverse of input string and the longest common subsequence of these two strings is the longest palindromic subsequence of the given string.
        
        def recur(i1,i2):
            if(i1<0 or i2<0):
                return 0
            if((i1,i2) in cache):
                return cache[(i1,i2)]
            if(s[i1]==t[i2]):
                res = 1+recur(i1-1,i2-1)
                cache[(i1,i2)] = res
                return res
            p1 = recur(i1-1,i2)
            p2 = recur(i1,i2-1)
            res = max(p1,p2)
            cache[(i1,i2)] = res
            return res
        
        cache =dict()
        return recur(len(s)-1,len(s)-1)
            
            
        