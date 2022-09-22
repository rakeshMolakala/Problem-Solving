class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        res = ""
        for c in s:
            if c!=" ":
                temp = c+temp
            else:
                res = res+" "+temp
                temp = ""
        res = res + " " +temp
        return res[1:]
        