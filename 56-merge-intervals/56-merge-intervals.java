class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(a,b) -> Integer.compare(a[0],b[0]));
        List<int[]> res = new ArrayList<>();
        
        int[] prevInterval = intervals[0];
        for (int i=1; i<intervals.length; i++){
            int prevStart = prevInterval[0];
            int prevEnd = prevInterval[1];
            
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            
            // If the curr interval and prev interval is not overlapping, we add the prev interval to result.
            if(prevEnd<currStart){
                res.add(prevInterval);
                prevInterval = intervals[i];
            }
            
            // If they are overlapping, we will merge them and change our prev interval to merged interval
            else{
                prevInterval[0] = Math.min(prevStart,currStart);
                prevInterval[1] = Math.max(prevEnd,currEnd);
            }
        }
        
        res.add(prevInterval);
        
        int[][] result = new int[res.size()][2];
        for(int i=0;i<res.size();i++){
            result[i] = res.get(i);
        }
        
        return result;
        
    }
}