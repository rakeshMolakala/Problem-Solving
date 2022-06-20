class TrieNode{
    Map<Character, TrieNode> children;
    boolean wordEnd;
    
    public TrieNode() {
        this.children = new HashMap<>();
        this.wordEnd = false;
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode curr = root;
        
        for(int i =0;i<word.length();i++){
            char temp = word.charAt(i);
            if(!curr.children.containsKey(temp)){
                curr.children.put(temp, new TrieNode());
            }
            curr = curr.children.get(temp);
        }
        curr.wordEnd = true;
    }
    
    public boolean search(String word) {
        TrieNode curr = root;
        
        for(int i = 0; i<word.length(); i++){
            char temp = word.charAt(i);
            if(!curr.children.containsKey(temp)){
                return false;
            }
            curr = curr.children.get(temp);
        }
        return curr.wordEnd;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        
        for(int i = 0; i<prefix.length(); i++){
            char temp = prefix.charAt(i);
            if(!curr.children.containsKey(temp)){
                return false;
            }
            curr = curr.children.get(temp);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */