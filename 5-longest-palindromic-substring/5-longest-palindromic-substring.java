// class Solution {
//     public String longestPalindrome(String s) {
//         String res = "";
//         int n = s.length();
//         boolean[][] dp = new boolean[n][n];
        
//         for(int i =n-1;i>-1;i--){
//             for(int j=i;j<n;j++){
//                 if(j-i==0){
//                     dp[i][j] = true;
//                 }
//                 else if(j-i<=2){
//                     dp[i][j] = s.charAt(i)==s.charAt(j);
//                 }
//                 else {
//                     dp[i][j] = (dp[i+1][j-1]) && (s.charAt(i)==s.charAt(j));
//                 }
//                 if(dp[i][j] && j-i+1>res.length()){
//                     res = s.substring(i,j+1);
//                 }
//             }
//         }
//         return res;
//     }
    
// }




class Solution {
    public String longestPalindrome(String s) {
        int res = 0;
        String ans = "";
        int[][] dp = new int[s.length()][s.length()];
        for(int i=0;i<s.length();i++){
            Arrays.fill(dp[i],-1);
        }
        
        for(int i =0;i<s.length();i++){
            for(int j=i;j<s.length();j++){
                if(isPalindrome(s,i,j,dp)){
                    if(j-i+1>res){
                        res = j-i+1;
                        ans = s.substring(i,j+1);
                    }
                }
            }
        }
        return ans;
    }
    
    public boolean isPalindrome(String s,int i,int j,int[][] dp){
        if(j-i==0){
            return true;
        }
        if(j-i==1 || j-i==2){
            return s.charAt(i)==s.charAt(j);
        }
        if(dp[i][j]!=-1){
            if(dp[i][j]==0){
                return false;
            }
            return true;
        }
        boolean temp = (isPalindrome(s,i+1,j-1,dp)) && (s.charAt(i)==s.charAt(j));
        if(temp){
            dp[i][j]=1;
        }
        else{
            dp[i][j]=0;
        }
        return temp;
    }
}