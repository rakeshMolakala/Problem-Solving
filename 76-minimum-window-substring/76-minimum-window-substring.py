## watched Neetcode video
class Solution:
    # very difficult one
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        countT = {}
        for x in t:
            countT[x] = 1 + countT.get(x,0)
        have = 0
        need = len(countT)
        res = [-1,1]
        resVal = math.inf
        
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)
            
            if(c in countT and window[c]==countT[c]):
                have = have + 1
            
            while(have==need):
                if(r-l+1 < resVal):
                    res = [l,r]
                    resVal = r-l+1
                
                window[s[l]]-=1
                if(s[l] in countT and window[s[l]]<countT[s[l]]):
                    have = have -1
                l= l + 1
        
        if(resVal == math.inf):
            return ""
        l,r = res
        resString = s[l:r+1]
        return resString
                
        