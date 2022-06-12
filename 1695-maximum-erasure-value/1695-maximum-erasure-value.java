class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        int[] prefsum = new int[nums.length];
        prefsum[0] = nums[0];
        for(int i =1;i<nums.length;i++){
            prefsum[i] = nums[i] +prefsum[i-1];
        }
        System.out.println(Arrays.toString(prefsum));
        
        int start = 0;
        int res2 = 0;
        for(int i =0;i<nums.length;i++){
            // if(!map.containsKey(nums[i])){
            //     tempSum = tempSum + nums[i];
            //     res = Math.max(res,tempSum);
            // }
            // else if (map.containsKey(nums[i]) && start<=map.get(nums[i])){
            //     start = map.get(nums[i]) + 1;
            // }
            if(map.containsKey(nums[i]) && start<=map.get(nums[i])) {
                start = map.get(nums[i]) + 1;
            }
            // else{
            //     int currSum = prefsum[i] - prefsum[start] + nums[start];
            //     res2 = Math.max(currSum,res2);
            // }
            map.put(nums[i],i);
            int currSum = prefsum[i] - prefsum[start] + nums[start];
            res2 = Math.max(currSum,res2);
        }
        return res2;
    }
}