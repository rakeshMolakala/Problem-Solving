class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()<2){
            return s.length();
        }
        Map<Character,Integer> map = new HashMap<>();
        int res = 1;
        int start = 0;
        map.put(s.charAt(0),0);
        for(int i =1;i<s.length();i++){
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