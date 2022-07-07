class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def recur(i,j):
            
            if(j<0 and i>=0):
                return False
            if(i<0 and j<0):
                return True
            if(i<0 and j>=0):
                temp = p[:j+1]
                if(len(temp)%2!=0):
                    return False
                for i in range(len(temp)):                       
                    if(i%2!=0 and temp[i]!="*"):
                        return False
                return True

                
            if((i,j) in cache):
                return cache[(i,j)]
            
            res = False
            if(s[i]==p[j] or p[j]=="."):
                res = recur(i-1,j-1)
            elif(p[j]=="*"):
                prev = p[j-1]
                p1 = recur(i,j-2)
                p2 = False
                if(prev==s[i] or prev=="."):
                    p2 = recur(i-1,j)
                res = p1 or p2
            cache[(i,j)] = res
            return res
        
    
        cache = dict()
        return recur(len(s)-1,len(p)-1)