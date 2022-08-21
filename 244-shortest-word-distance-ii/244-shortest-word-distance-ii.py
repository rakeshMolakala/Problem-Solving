class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.track = collections.defaultdict(list)
        for i,word in enumerate(wordsDict):
            self.track[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        res = math.inf
        l1 = self.track[word1]
        l2 = self.track[word2]
        n1 = len(l1)
        n2 = len(l2)
        p1,p2 = 0,0
        while(p1<n1 and p2<n2):
            first = l1[p1]
            second = l2[p2]
            res = min(res,abs(first-second))
            if(first<second):
                p1+=1
            else:
                p2+=1
        return res
        
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)