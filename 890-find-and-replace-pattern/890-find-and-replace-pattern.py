class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        def matches(word, pattern):
            map1 = dict()
            map2 = dict()
            
            for i in range(len(word)):
                w = word[i]
                p = pattern[i]
                if w not in map1:
                    map1[w] = p
                if p not in map2:
                    map2[p] = w
                if p!=map1[w] or w!=map2[p]:
                    return False
            return True
        
        res = []
        for word in words:
            if(matches(word,pattern)):
                res.append(word)
        return res
        