class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = math.inf
        n = len(wordsDict)
        first, second  = -1,-1
        if(word1==word2):
            prev=-1
            for i in range(n):
                if(wordsDict[i]==word1):
                    if(prev!=-1):
                        res = min(res,abs(prev - i))
                    prev = i
            return res
                    
        for i in range(n):
            if wordsDict[i]==word1:
                first = i
            elif wordsDict[i]==word2:
                second = i
            if(first!=-1 and second !=-1):
                res = min(res,abs(second - first))
        return res
        
        
#         res = math.inf
#         track = collections.defaultdict()
#         for i,word in wordsDict:
#             track[word].append(i)
            
#         l1 = track[word1]
#         l2 = track[word2]