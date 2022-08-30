class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = collections.defaultdict(list)
        for s in strs:
            temp = [0]*26
            for c in s:
                index = ord(c) - ord('a')
                temp[index]+=1
            track[tuple(temp)].append(s)
        
        return track.values()
        