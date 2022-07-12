class TrieNode:
    def __init__(self):
        # dict of character to TrieNode
        self.children = dict()
        self.wordEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.wordEnd = True
                

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.wordEnd 
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)