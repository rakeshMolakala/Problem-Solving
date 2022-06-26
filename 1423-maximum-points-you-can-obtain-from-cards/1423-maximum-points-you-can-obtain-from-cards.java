class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int wsize = n-k;
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
            wsum = wsum-cardPoints[i]+cardPoints[wsize+i];
            res = Math.min(wsum,res);
        }
        return tsum - res;
        
    }
}