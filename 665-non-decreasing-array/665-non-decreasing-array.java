class Solution {
    public boolean checkPossibility(int[] nums) {
        int violations=0;
        for(int i =1;i<nums.length;i++){
            if(nums[i-1]>nums[i]){
                if(violations==1){
                    return false;
                }
                else{
                    if(i-2<0){
                        nums[i-1] = nums[i];
                    }
                    else{
                        if(nums[i-2]<=nums[i]){
                            nums[i-1] = nums[i];
                        }
                        else{
                            nums[i] = nums[i-1];
                        }
                    }
                    violations++;
                }
            }
        }
        return true;
    }
}