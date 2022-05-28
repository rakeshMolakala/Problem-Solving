class Solution {
    
    private int[][] direc = {{0,1},{1,0},{-1,0},{0,-1}};
    private int l = 0;
    private int b = 0;
    private char[][] board = null;
    
    public boolean exist(char[][] board, String word) {
        l = board.length;
        b = board[0].length;
        this.board = board;
        
        for(int i =0;i<l;i++){
            for (int j=0;j<b;j++){
                if(board[i][j]==word.charAt(0) && search(i,j,1,word)){
                    return true; 
                }
            }
        }
        return false;
    }
    
    
    public boolean search(int r,int c,int index, String word){
        
        if(index==word.length()){
            return true;
        }
        
        board[r][c] = '$';
        boolean found = false;
        for(int i =0;i<direc.length;i++) {
            int tempx = r+direc[i][0];
            int tempy = c+direc[i][1];
            if(tempx>=0 && tempx<l && tempy>=0 && tempy<b && board[tempx][tempy]==word.charAt(index)) {
                if(search(tempx,tempy,index+1,word)){
                    found = true;
                    break;
                }
            }  
        }
              
        board[r][c] = word.charAt(index-1);
        return found;
                             
    }
                   
                   
}