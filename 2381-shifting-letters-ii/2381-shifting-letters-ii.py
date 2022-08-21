class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Brute force
#         res = ""
#         track = collections.defaultdict(int)
#         n = len(s)
#         direcMap = {0:-1, 1:1}
        
#         for start, end, direc in shifts:
#             for i in range(start,end+1):
#                 track[i] = track[i] + direcMap[direc]
#         print(track)  
#         for i in range(len(s)):
#             res = res + self.shift(s[i],track[i])
#         return res
        
        # using prefix sum approach
        n = len(s)
        res = ""
        prefix_sum = [0]*(n+1)
        for start,end,direc in shifts:
            if(direc==1):
                prefix_sum[start] = prefix_sum[start] + 1
                prefix_sum[end + 1] = prefix_sum[end+1] - 1
            else:
                prefix_sum[start] = prefix_sum[start] - 1
                prefix_sum[end + 1] = prefix_sum[end+1] + 1
        
        for i in range(n):
            if i==0:
                res = res + self.shift(s[i],prefix_sum[0])
                continue
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]
            res = res + self.shift(s[i],prefix_sum[i])
        return res
            
        
    def shift(self,c,steps):
        if(steps==0):
            return c
        if(steps>0):
            newAscii = (ord(c) - ord('a') + steps) % 26
            return chr(newAscii + ord('a'))
        else:
            newAscii = (ord(c) - ord('a') + steps) % 26
            newAscii = (newAscii + 26)%26
            return chr(newAscii + ord('a'))
            
            
            
        