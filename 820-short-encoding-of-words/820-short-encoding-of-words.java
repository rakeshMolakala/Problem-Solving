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
    
    public boolean isPrefixOfOtherWords(String prefix) {
        TrieNode curr = root;
        
        for(int i = 0; i<prefix.length(); i++){
            char temp = prefix.charAt(i);
            if(!curr.children.containsKey(temp)){
                return false;
            }
            curr = curr.children.get(temp);
        }
        return curr.children.size()>0;
    }
}

class Solution {
    public int minimumLengthEncoding(String[] words) {
        Trie trie = new Trie();
        Set<String> set = new HashSet<>();
        int res = 0;
        for(int i =0;i<words.length;i++){
            StringBuilder sb = new StringBuilder(words[i]);  
            sb.reverse(); 
            set.add(sb.toString());
            trie.insert(sb.toString());  
        }
        for(String s: set){
            if(!trie.isPrefixOfOtherWords(s)){
                res = res + s.length()+1;
            }
        }
        return res;
        
    }
}