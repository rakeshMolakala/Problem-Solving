class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2!=0:
            return []
        
        res =[]
        
        track = collections.defaultdict(int)
        for num in changed:
            track[num]+=1
            
        for num in sorted(track.keys()):
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