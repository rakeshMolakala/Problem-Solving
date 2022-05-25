class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(a,b) -> Integer.compare(a[0],b[0]));
        List<int[]> res = new ArrayList<>();
//         for(int i =0;i<intervals.length;i++){
//             System.out.println(intervals[i][0]+" - "+intervals[i][1]);
            
//         }
        
        int[] prevInterval = intervals[0];
        for (int i=1; i<intervals.length; i++){
            int prevStart = prevInterval[0];
            int prevEnd = prevInterval[1];
            
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            
            if(prevEnd<currStart){
                res.add(prevInterval);
                prevInterval = intervals[i];
            }
            else{
                int newStart = Math.min(prevStart,currStart);
                int newEnd = Math.max(prevEnd,currEnd);
                prevInterval[0] = newStart;
                prevInterval[1] = newEnd;
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