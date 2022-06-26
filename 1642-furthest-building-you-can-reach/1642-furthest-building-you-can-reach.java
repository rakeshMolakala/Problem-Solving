class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        int res = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i=1;i<heights.length;i++){
            int diff = heights[i]-heights[i-1];
            if(diff<=0){
                res++;
                continue;
            }
            if(bricks>=diff){
                bricks=bricks-diff;
                pq.add(diff);
                res++;
                continue;
            }
            else if(ladders==0){
                break;
            }
            else{
                if(pq.size()==0){
                    ladders=ladders-1;
                    res++;
                }
                else{
                    if(pq.peek()>=diff){
                        bricks = bricks+pq.poll()-diff;
                        ladders = ladders -1 ;
                        pq.add(diff);
                    }
                    else{
                        ladders=ladders-1;
                    }
                    res++;
                }
            }
            
        }
        return res;
    }
}