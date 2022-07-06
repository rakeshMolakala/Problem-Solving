class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def recur(i1,i2,):
            if(i1<0 or i2<0):
                return 0
            if((i1,i2) in cache):
                return cache[(i1,i2)]
            if(word1[i1]==word2[i2]):
                cache[(i1,i2)] = 1+recur(i1-1,i2-1)
                return cache[(i1,i2)]
            p1 = recur(i1,i2-1)
            p2 = recur(i1-1,i2)
            cache[(i1,i2)] = max(p1,p2)
            return max(p1,p2)
        
        cache = dict()
        common = recur(len(word1)-1,len(word2)-1)
        w1_del = len(word1)-common
        w2_del = len(word2)-common
        return w1_del+w2_del
        
        
        