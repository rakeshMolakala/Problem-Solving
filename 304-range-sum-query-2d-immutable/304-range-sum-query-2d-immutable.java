class NumMatrix {
    private int[][] matrix;

    public NumMatrix(int[][] matrix) {
        this.matrix = matrix;
        for(int i =0;i<matrix.length;i++){
            for(int j =1;j<matrix[0].length;j++){
                matrix[i][j] = matrix[i][j-1]+matrix[i][j];
            }
        }
        
        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int res=0;
        for(int i = row1;i<row2+1;i++){
            if(col1>0){
                res = res + matrix[i][col2] - matrix[i][col1-1];
            }
            else{
                res = res + matrix[i][col2];
            }
        }
        return res;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */