class Solution {
    public boolean checkValid(int[][] matrix) {
        //check every row
        int n=matrix.length;
        for(int i = 0;i<n;i++){
            Set<Integer> set1 = new HashSet<>();
            Set<Integer> set2 = new HashSet<>();
            for(int j=0;j<n;j++) {
                //row wise search
                set1.add(matrix[i][j]);
                
                //column wise search
                set2.add(matrix[j][i]);
            }
            if(set1.size()!=n || set2.size()!=n){
                return false;
            }
        }
        
        return true;
        
    }
}