class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def recur(i1,i2):
            if(i1<0 or i2<0):
                return 0
            if((i1,i2) in cache):
                return cache[(i1,i2)]
            if(text1[i1]==text2[i2]):
                return 1+recur(i1-1,i2-1)
            p1 = recur(i1,i2-1)
            p2 = recur(i1-1,i2)
            cache[(i1,i2)] = max(p1,p2)
            return max(p1,p2)
        
        cache = dict()
        return recur(len(text1)-1,len(text2)-1)