class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int len = nums.length;
        for(int i =0;i<nums.length;i++){
            sum=sum+nums[i];
        }
        return len*(len+1)/2 - sum;
    }
}