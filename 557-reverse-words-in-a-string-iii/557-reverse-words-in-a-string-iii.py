class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        res = ""
        for c in s:
            if c==" ":
                res = res +temp+" "
                temp = ""
            else:
                temp = c+temp

        res = res + temp
        return res
        