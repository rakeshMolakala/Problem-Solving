class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # recur(i,j) represents whether s3[i+j:] is an interleaving string formed by s1[i:] and s2[j:]
        def recur(i,j):
            # it is the pointer on s3 string
            k = i+j           
            
            # base cases
            if(i==len(s1)):
                return s2[j:]==s3[k:]
            if(j==len(s2)):
                return s1[i:]==s3[k:]
            
            if((i,j) in cache):
                return cache[(i,j)]
            
            res = False
            if(s3[k]==s1[i]==s2[j]):
                p1 = recur(i+1,j)
                p2 = recur(i,j+1)
                res = p1 or p2
            elif(s3[k]==s1[i]):
                res = recur(i+1,j)
            elif(s3[k]==s2[j]):
                res = recur(i,j+1)
            cache[(i,j)] = res
            return res
        
        cache = dict()
        if(len(s3)!=len(s1)+len(s2)):
            return False
        return recur(0,0)