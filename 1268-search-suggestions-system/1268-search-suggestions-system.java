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
    
    public void dfs(String word, TrieNode curr, List<String> res){
        if(curr.children.size()==0){
            res.add(word);
            return;
        }
        if(curr.wordEnd){
            res.add(word);
        }
        for(Map.Entry<Character,TrieNode> entry: curr.children.entrySet()){
            dfs(word+String.valueOf(entry.getKey()), entry.getValue(),res);
        }
    }
    
    
}



class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        List<List<String>> res = new ArrayList<>();
        Trie trie = new Trie();
        for(int i =0;i<products.length;i++){
            trie.insert(products[i]);
        }
        
        
        for(int i =1;i<searchWord.length()+1;i++){
            String temp = searchWord.substring(0,i);
            List<String> tempres = new ArrayList<>();
            TrieNode curr = trie.root;
            boolean subFound = true;
            for(int j =0;j<temp.length();j++){
                char tempChar = temp.charAt(j);
                if(!curr.children.containsKey(tempChar)){
                    subFound = false;
                    break;
                }
                curr = curr.children.get(tempChar);
            }
            if(subFound){
                trie.dfs(temp,curr,tempres);
                Collections.sort(tempres);
            }
            
            List<String> tempres2 = new ArrayList<>();
            int n = 0;
            for(String s : tempres){
                tempres2.add(s);
                n++;
                if(n==3){
                    break;
                }
            }
            res.add(tempres2);
        }
        
        return res;
        
        
        
        
        
        
    }
}