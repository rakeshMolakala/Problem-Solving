class Solution {
    public int searchInsert(int[] nums, int target) {
        if(target<nums[0]){
            return 0;
        }
        if(target>nums[nums.length-1]){
            return nums.length;
        }
        
        return binarySearch(nums,0,nums.length-1,target);
    }
    
    public int binarySearch(int[] nums, int i,int j,int target){
        int mid = (i+j)/2;
        if(nums[mid]==target){
            return mid;
        }
        if(j==i+1){
            return j;
        }
        if(target>nums[mid]){
            return binarySearch(nums,mid,j,target);
        }
        else{
            return binarySearch(nums,i,mid,target);
        }
        
    }
}