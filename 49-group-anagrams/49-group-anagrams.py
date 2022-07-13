from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        track = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for c in s:
                index = ord(c) - ord('a')
                count[index] +=1
            track[tuple(count)].append(s)
        
        return track.values()
                
        
        