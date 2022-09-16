class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        // For Right Pointer
        int n = nums.length;
        // Number of Operations
        int m = multipliers.length;
        int[] dp = new int[m + 1];
        
        for (int op = m - 1; op >= 0; op--) {
            int[] next_row = dp.clone();
            // Present Row is now next_Row because we are moving upwards
            for (int left = op; left >= 0; left--) {
                dp[left] = Math.max(multipliers[op] * nums[left] + next_row[left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + next_row[left]);
            }
        }
        
        return dp[0];
    }
}





// class Solution {
//     public int maximumScore(int[] nums, int[] multipliers) {
//         int n = nums.length;
//         int m = multipliers.length;
//         Map<String,Integer> map = new HashMap<>();
//         return recur(nums,multipliers,n,m,0,n-1,map);
        
//     }
    
//     private int recur(int[] nums, int[] multipliers, int n, int m, int i, int j, Map<String,Integer> map){
//         int k = n - (j-i+1);
//         if(k==m){
//             return 0;
//         }
//         String temp = i+","+j;
//         if (map.containsKey(temp)){
//             return map.get(temp);
//         }
//         int p1 = multipliers[k]*nums[i] + recur(nums,multipliers,n,m,i+1,j,map);
//         int p2 = multipliers[k]*nums[j] + recur(nums,multipliers,n,m,i,j-1,map);
//         int res = Math.max(p1,p2);
//         map.put(temp,res);
//         return res;
//     }
// }