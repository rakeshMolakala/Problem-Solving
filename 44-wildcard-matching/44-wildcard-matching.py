class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def recur(i,j):
            if(i<0 and j<0):
                return True
            if(i<0 and j>=0):
                for x in p[:j+1]:
                    if(x!="*"):
                        return False
                return True
            if(j<0 and i>=0):
                return False
        
            if((i,j) in cache):
                return cache[(i,j)]
            
            res = False
            if(s[i]==p[j] or p[j]=="?"):
                res = recur(i-1,j-1)
            elif (p[j]=="*"):
                p1 = recur(i-1,j)
                p2 = recur(i,j-1)
                res = p1 or p2
            
            cache[(i,j)] = res
            return res
            
        cache = dict()
        return recur(len(s)-1,len(p)-1)
          