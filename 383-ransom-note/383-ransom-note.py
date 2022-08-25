class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0]*26
        for c in magazine:
            index = ord(c) - ord('a')
            arr[index] += 1
        
        for c in ransomNote:
            index = ord(c) - ord('a')
            arr[index] -= 1
            if(arr[index]<0):
                return False
        return True
        