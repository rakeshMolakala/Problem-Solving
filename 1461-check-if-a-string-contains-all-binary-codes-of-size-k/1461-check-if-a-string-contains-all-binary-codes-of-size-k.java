class Solution {
    public boolean hasAllCodes(String s, int k) {
        Set<Integer> set = new HashSet<>();
        for(int i=0;i<s.length()-k+1;i++){
            String temp = s.substring(i,i+k);
            set.add(Integer.parseInt(temp,2));
        }
        System.out.println(set);
        int req = (int) Math.pow(2,k);
        for(int i =0;i<req;i++){
            if(!set.contains(i)){
                return false;
            }
        }
        return true;
    }
}