class Solution:
    def firstUniqChar(self, s: str) -> int:
        track = collections.defaultdict(int)
        for c in s:
            track[c] = track[c] + 1
        for i in range(len(s)):
            if track[s[i]]==1:
                return i
        return -1
        