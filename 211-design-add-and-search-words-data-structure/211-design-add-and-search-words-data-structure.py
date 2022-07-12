class TrieNode:
    def __init__(self):
        # dict of character to TrieNode
        self.children = dict()
        self.wordEnd = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.wordEnd = True
        

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            curr = root
            for i in range(j,len(word)):
                if word[i]=='.':
                    for child in curr.children.values():
                        if(dfs(i+1,child)):
                            return True
                    return False
                    
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.wordEnd
        
        return dfs(0,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)