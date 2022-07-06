class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def recur(i,j):
            if(j>i):
                return 0
            if(j<0):
                return 1
            if((i,j) in cache):
                return cache[(i,j)]

            res = 0
            if(s[i]==t[j]):
                p1 = recur(i-1,j-1)
                p2 = recur(i-1,j)
                res = p1+p2
            else:
                res = recur(i-1,j)
            cache[(i,j)] = res
            return res
        
        cache = dict()
        return recur(len(s)-1,len(t)-1)
        