class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        setList = []
        n=len(words)
        for i in range(n):
            setList.append(set(words[i]))
        for i in range(n):
            for j in range(i+1,n):
                if(not(setList[i] & setList[j])):
                    res = max(res,len(words[i])*len(words[j]))
        return res