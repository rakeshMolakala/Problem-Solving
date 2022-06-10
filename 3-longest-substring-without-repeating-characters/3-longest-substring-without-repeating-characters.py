class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        usedChars = {}
        for i in range(len(s)):
            if s[i] in usedChars and start <= usedChars[s[i]]:
                start = usedChars[s[i]] + 1
            else: 
                longest = max(longest , i-start +1)
            usedChars[s[i]] = i
        return longest