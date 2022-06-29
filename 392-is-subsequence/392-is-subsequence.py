class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)==0):
            return True
        p1=0
        p2=0
        while(p1<len(s) and p2<len(t)):
            if(s[p1]==t[p2]):
                if(p1==len(s)-1):
                    return True
                p1=p1+1
                p2=p2+1
            else:
                p2=p2+1
            
        return False