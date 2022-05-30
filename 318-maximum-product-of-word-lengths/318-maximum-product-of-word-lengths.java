class Solution {
    public int maxProduct(String[] words) {
        int n = words.length;
        int res = 0;
        List<Set<Character>> setList = new ArrayList<>();
        for(int i =0;i<n;i++){
            Set<Character> tempSet = new HashSet<>();
            for(int j=0;j<words[i].length();j++){
                tempSet.add(words[i].charAt(j));
            }
            setList.add(tempSet);
        }
        
        for(int i =0;i<n;i++){
            for(int j=i+1;j<n;j++){
                Set<Character> set1 = setList.get(i);
                Set<Character> set2 = setList.get(j);
                Set<Character> temp = new HashSet<>(set1);
                temp.retainAll(set2);
                if(temp.size()==0){
                    res = Math.max(res,words[i].length()*words[j].length());
                }
            }
        }
        return res;
        
    }
}