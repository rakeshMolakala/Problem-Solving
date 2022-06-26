class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i =0;i<nums.length;i++){
            pq.add(nums[i]);
        }
        int res = 0;
        for(int i = 0; i<k;i++){
            res = pq.poll();
        }
        return res;
    }
}