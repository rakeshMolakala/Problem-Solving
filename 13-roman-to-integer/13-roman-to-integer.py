class Solution:
    def romanToInt(self, s: str) -> int:
        track = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        res = track[s[n-1]]
        
        for i in range(n-1):
            if(s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X')):
                res = res - track[s[i]]
            elif(s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C')):
                res = res - track[s[i]]
            elif(s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M')):
                res = res - track[s[i]] 
            else:
                res = res + track[s[i]]
        return res       
                