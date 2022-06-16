class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        Map<String,Integer> map = new HashMap<>();
        recur(triangle,0,0,map);
        if(triangle.size()==1){
            return triangle.get(0).get(0);
        }
        return map.get("0,0");
    }
    
    public int recur(List<List<Integer>> triangle,int i,int j, Map<String,Integer> map){
        if(j>triangle.get(i).size()-1 || i>triangle.size()-1){
            return 0;
        }
        if(i==triangle.size()-1){
            return triangle.get(i).get(j);
        }
        String temp = i+","+j;
        if(map.containsKey(temp)){
            return map.get(temp);
        }
        int tempRes = Math.min(triangle.get(i).get(j)+recur(triangle,i+1,j,map),triangle.get(i).get(j)+recur(triangle,i+1,j+1,map));
        map.put(temp,tempRes);
        return tempRes;
        
    }
}