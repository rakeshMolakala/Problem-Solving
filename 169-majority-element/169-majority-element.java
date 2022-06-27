class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int target = nums.length/2;
        int c = 1;
        for(int i = 1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
                c++;
            }
            else{
                if(c>target){
                    return nums[i-1];
                }
                else{
                    c=1;
                }
            }
        }
        return nums[nums.length-1];
    }
}