class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = dict()
        n = len(s)
        start  = 0
        res = 0
        for i in range(n):
            if s[i] in track and track[s[i]]>=start:
                start = track[s[i]] + 1
            else:                      
                res = max(res,i-start+1)
            track[s[i]] = i
            
        return res       