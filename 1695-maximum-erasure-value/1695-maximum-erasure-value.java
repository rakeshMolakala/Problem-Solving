class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        int[] prefsum = new int[nums.length];
        prefsum[0] = nums[0];
        for(int i =1;i<nums.length;i++){
            prefsum[i] = nums[i] +prefsum[i-1];
        }        
        int start = 0;
        int res = 0;
        for(int i =0;i<nums.length;i++){
            if(map.containsKey(nums[i]) && start<=map.get(nums[i])) {
                start = map.get(nums[i]) + 1;
            }
            map.put(nums[i],i);
            int currSum = prefsum[i] - prefsum[start] + nums[start];
            res = Math.max(currSum,res);
        }
        return res;
    }
}