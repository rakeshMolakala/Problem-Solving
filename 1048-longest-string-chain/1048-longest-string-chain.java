class Solution {
    public int longestStrChain(String[] words) {
        Set<String> set = new HashSet<>();
        for(int i =0;i<words.length;i++){
            set.add(words[i]);
        }
        Map<String,Integer> map = new HashMap<>();
        int res = 0;
        for(int i =0;i<words.length;i++){
            res = Math.max(dfs(words[i],set,map),res);
        }
        return res;
    }
    
    
    public int dfs(String s, Set<String> set, Map<String,Integer> map){
        if(!set.contains(s)){
            return 0;
        }
        if(s.length()==1){
            return 1;
        }
        if(map.containsKey(s)){
            return map.get(s);
        }
        int tempRes = 0;
        for(int i=0;i<s.length();i++){
            String temp = s.substring(0,i)+s.substring(i+1,s.length());
            tempRes = Math.max(tempRes,1+dfs(temp,set,map));
        }
        map.put(s,tempRes);
        return tempRes;
    }
}