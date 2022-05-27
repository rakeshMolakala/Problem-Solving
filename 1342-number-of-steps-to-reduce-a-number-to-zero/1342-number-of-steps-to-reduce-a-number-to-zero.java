class Solution {
    public int numberOfSteps(int num) {
        int res = 0;
        if(num==0){
            return res;
        }
        while(true){
            if(num%2==0){
                num = num/2;
            }
            else{
                num--;
            }
            res++;
            if(num==0){
                return res;
            }
        }
    }
}