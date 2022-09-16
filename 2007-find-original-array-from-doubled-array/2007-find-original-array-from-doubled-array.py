class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
#         n = len(changed)
#         if n%2!=0:
#             return []
#         track = collections.defaultdict(int)
#         for num in changed:
#             track[num]+=1
        
#         res = []
#         changed.sort()
        
#         for num in changed:
#             if track[num]>0:
#                 track[num]-=1
                
#                 if 2*num in track:
#                     track[2*num]-=1
#                     res.append(num)
#                 else:
#                     return []
        
#         if len(res)==n//2:
#             return res
#         return []
        
        
        n = len(changed)
        if n%2!=0:
            return []
        
        res =[]
        
        track = collections.defaultdict(int)
        for num in changed:
            track[num]+=1
            
        temp = list(track.keys())
        temp.sort()
            
        for num in temp:
            if track[num]>0:
                
                if num==0:
                    count = track[num]
                    if count%2!=0:
                        return []
                    res = res + [0]*(count//2)
                    track[num] = track[num] - count
                
                elif 2*num in track:
                    count = track[num]
                    double_count = track[2*num]
                    if double_count<count:
                        return []
                    res = res + [num]*(count)
                    track[num] = track[num] - count
                    track[2*num] = track[2*num] - count
                    
                else:
                    return []
        
        if len(res)==n//2:
            return res
        return []