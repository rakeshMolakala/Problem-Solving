class Solution {
    public int lengthOfLIS(int[] nums) {
        int res = 0;
        int[] dp = new int[nums.length];
        // dp[i] is the length of LCS upto that point of array where dp[i] is in the LCS
        
        for(int i = 0;i<nums.length;i++){
            int prevMax = 0;
            for(int j = 0;j<i;j++){
                if(nums[i]>nums[j]){
                    prevMax = Math.max(prevMax,dp[j]);
                }
            }
            dp[i]=prevMax+1;
            res = Math.max(res,dp[i]);
        }
        
        return res;
        
    }
}