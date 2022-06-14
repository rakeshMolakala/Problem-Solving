class Solution {
    public int minDistance(String word1, String word2) {
        int[][] memo = new int[word1.length()][word2.length()];
        for(int i =0;i<word1.length();i++){
            Arrays.fill(memo[i],-1);
        }
        
        return word1.length()+word2.length()-2*(recur(word1,word2,word1.length(),word2.length(),memo));
    }
    
    
    public int recur(String s1, String s2, int i,int j,int[][] memo){
        if(i==0 || j==0){
            return 0;
        }
        if(memo[i-1][j-1]!=-1){
            return memo[i-1][j-1];
        }
        
        if(s1.charAt(i-1)==s2.charAt(j-1)){
            memo[i-1][j-1] = 1+recur(s1,s2,i-1,j-1,memo);
        }
        else{
            memo[i-1][j-1] = Math.max(recur(s1,s2,i-1,j,memo),recur(s1,s2,i,j-1,memo));
        }
        return memo[i-1][j-1];
        
    }
}