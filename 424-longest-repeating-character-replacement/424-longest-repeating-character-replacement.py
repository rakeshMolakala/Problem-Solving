from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        res = 0
        l = 0
        r =0
        while(r<len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            
            # if window is not valid we keep reducing the window size till we get valid one
            while((r-l+1) - max(count.values())>k):
                count[s[l]]-=1
                l=l+1
            res = max(res,(r-l+1))
            r+=1
                
        return res