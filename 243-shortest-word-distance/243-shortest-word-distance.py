class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = math.inf
        n = len(wordsDict)
        first, second  = -1,-1
        for i in range(n):
            if wordsDict[i]==word1:
                first = i
            elif wordsDict[i]==word2:
                second = i
            if(first!=-1 and second !=-1):
                res = min(res,abs(second - first))
        return res