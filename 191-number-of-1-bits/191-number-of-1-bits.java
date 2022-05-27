public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int mask = 1;
        int res = 0;
        for(int i=0;i<32;i++){
            if((mask & n)==1){
                res++;
            }
            n=n>>1;
        }
        return res;
    }
}