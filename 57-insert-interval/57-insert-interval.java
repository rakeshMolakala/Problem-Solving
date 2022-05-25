class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;
        List<int[]> res = new ArrayList<>();
        boolean intervalAdded = false;
        
        for(int i = 0;i<n;i++){
            if(intervalAdded){
                res.add(intervals[i]);
                continue;
            }
            
            int newStart = newInterval[0];
            int newEnd = newInterval[1];
            
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            
            if(newEnd<currStart){
                res.add(newInterval);
                res.add(intervals[i]);
                intervalAdded = true;
            }
            
            else if(newStart>currEnd){
                res.add(intervals[i]);
            }
             
            else{
                newInterval[0] = Math.min(newStart,currStart);
                newInterval[1] = Math.max(newEnd,currEnd);
            }
        }
        
        if(!intervalAdded) {
            res.add(newInterval);
        }
        
        int[][] result = new int[res.size()][2];
        for(int i=0;i<res.size();i++){
            result[i] = res.get(i);
        }
        return result;
        
        
        
    }
}