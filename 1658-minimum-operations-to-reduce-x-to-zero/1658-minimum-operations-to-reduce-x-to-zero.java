class Solution {
    public int minOperations(int[] nums, int x) {
        int sum = 0;
        for(int i =0;i<nums.length;i++){
            sum=sum+nums[i];
        }
        int target = sum - x;
        if(target<0){
            return -1;
        }
        if(target==0){
            return nums.length;
        }

        int i=0;
        int j=0;
        int temp =0;
        int max = 0;
        while(j<nums.length){
            temp = temp+nums[j];
            if(temp<target){
                j++;
            }
            else if (temp==target){
                max = Math.max(max,j-i+1);
                j++;
            }
            else{
                while(temp>target){
                    temp = temp - nums[i];
                    i++;
                }
                if(temp==target){
                    max = Math.max(max,j-i+1);
                }
                j++;
            }
        }
        if(max==0){
            return -1;
        }
        return nums.length-max;
    }
}