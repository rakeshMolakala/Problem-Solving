class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()<2){
            return s.length();
        }
        Map<Character,Integer> map = new HashMap<>();
        int start = 0;
        int res =0;
        for(int i =0;i<s.length();i++){
            if(map.containsKey(s.charAt(i)) && map.get(s.charAt(i))>=start){
                start = map.get(s.charAt(i))+1;   
            }
            else{
                res = Math.max(res,i-start+1);
                System.out.println(res);
            }
            
            map.put(s.charAt(i),i);
            
            
        }
        
        return res;
        
    }
}