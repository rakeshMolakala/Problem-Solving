class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def recur(i,j):
            if(i<0):
                return j+1
            if(j<0):
                return i+1
            
            if((i,j) in cache):
                return cache[(i,j)]
            
            res = 0
            if(word1[i]==word2[j]):
                res = 0 + recur(i-1,j-1)
            else:
                delete = 1 + recur(i-1,j)
                replace = 1 + recur(i-1,j-1)
                insert = 1 + recur(i,j-1)
                res = min(delete,insert,replace)
            cache[(i,j)] = res
            return res
        
        cache = dict()
        return recur(len(word1)-1,len(word2)-1)