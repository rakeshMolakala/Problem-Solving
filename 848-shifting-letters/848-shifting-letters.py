class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for i in range(n-2,-1,-1):
            shifts[i] = shifts[i] + shifts[i+1]
        res = ""
        for i in range(n):
            curr = ord(s[i]) - ord('a')
            curr = (curr + shifts[i]) % 26
            res = res + chr(curr + ord('a'))
        return res
        