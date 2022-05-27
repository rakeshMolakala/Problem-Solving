class Solution {
    public int countCharacters(String[] words, String chars) {
        int res = 0;
        Map<Character,Integer> map = new HashMap<>();
        for(int i =0;i<chars.length();i++){
            char temp = chars.charAt(i);
            if(map.containsKey(temp)){
                map.put(temp,map.get(temp)+1);
            }
            else{
                map.put(temp,1);
            }
        }
        
        for (int i = 0; i<words.length; i++){
            Map<Character,Integer> tempMap = new HashMap<>(map);
            String curr = words[i];
            boolean included = true;
            for(int j = 0;j<curr.length();j++){
                if(tempMap.containsKey(curr.charAt(j)) && tempMap.get(curr.charAt(j))>0){
                    tempMap.put(curr.charAt(j),tempMap.get(curr.charAt(j))-1);
                }
                else{
                    included = false;
                    break;
                }
            }
            if(included){
                res = res + curr.length();
            }
        }
        
        return res;
    }
}