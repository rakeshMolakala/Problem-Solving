class Solution {
    public int maxScore(int[] cardPoints, int k) {
        //This problem is to find the minimum subarray of length n-k
        int n = cardPoints.length;
        int window = n-k;
        int wsum = 0;
        int tsum = 0;
        for(int i =0;i<n-k;i++){
            wsum = wsum + cardPoints[i];
        }
        for(int i =0;i<n;i++){
            tsum = tsum + cardPoints[i];
        }
        int res = wsum;
        
        
        for(int i = 0; i<k; i++){
            wsum = wsum-cardPoints[i]+cardPoints[window+i];
            res = Math.min(wsum,res);
        }
        return tsum - res;
        
    }
}