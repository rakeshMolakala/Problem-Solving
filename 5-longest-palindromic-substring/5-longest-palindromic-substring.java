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
        String ans = "";
        int n = s.length();
        int[][] dp = new int[s.length()][s.length()];
        for(int i=0;i<n;i++){
            Arrays.fill(dp[i],-1);
        }
        
        for(int i =0;i<n;i++){
            for(int j=i;j<n;j++){
                if(isPalindrome(s,i,j,dp)==1){
                    if(j-i+1>ans.length()){
                        ans = s.substring(i,j+1);
                    }
                }
            }
        }
        return ans;
    }
    
    public int isPalindrome(String s,int i,int j,int[][] dp){
        if(j-i==0){
            return 1;
        }
        if(j-i<=2){
            if(s.charAt(i)==s.charAt(j)){
                return 1;
            }
            return 0;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        boolean temp = (isPalindrome(s,i+1,j-1,dp)==1) && (s.charAt(i)==s.charAt(j));
        if(temp){
            dp[i][j]=1;
        }
        else{
            dp[i][j]=0;
        }
        return dp[i][j];
    }
}