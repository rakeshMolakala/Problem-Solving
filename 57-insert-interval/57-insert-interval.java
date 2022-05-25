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
            
            int tempStart = intervals[i][0];
            int tempEnd = intervals[i][1];
            
            if(newEnd<tempStart){
                res.add(newInterval);
                res.add(intervals[i]);
                intervalAdded = true;
                continue;
            }
            
            else if(newStart>tempEnd){
                res.add(intervals[i]);
                continue;
            }
             
            else{
                newInterval[0] = Math.min(newStart,tempStart);
                newInterval[1] = Math.max(newEnd,tempEnd);
                System.out.println(newInterval[1]);
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