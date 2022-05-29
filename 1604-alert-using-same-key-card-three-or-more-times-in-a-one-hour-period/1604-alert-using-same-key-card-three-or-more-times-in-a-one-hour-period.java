class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        List<String> res = new ArrayList<>();
        Map<String,List<Integer>> map = new HashMap<>();
        for(int i =0;i<keyTime.length;i++){
            if(map.containsKey(keyName[i])){
                map.get(keyName[i]).add(calTime(keyTime[i]));
            }
            else{
                List<Integer> temp = new ArrayList<>();
                temp.add(calTime(keyTime[i]));
                map.put(keyName[i],temp);
            }
        }
        
        for(Map.Entry<String,List<Integer>> entry: map.entrySet()){
            Collections.sort(entry.getValue());
            List<Integer> temp = entry.getValue();
            for(int i =1;i<temp.size()-1;i++){
                if(temp.get(i+1)-temp.get(i-1)<=60){
                    res.add(entry.getKey());
                    break;
                }
            }
        }
        Collections.sort(res);
        return res;
    }
    
    
    public int calTime(String str){
        int h = Integer.valueOf(str.substring(0,2));
        int m = Integer.valueOf(str.substring(3,5));
        return h*60+m;
    }
}