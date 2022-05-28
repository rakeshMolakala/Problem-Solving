class Solution {
    
    private int[][] direc = {{0,1},{1,0},{-1,0},{0,-1}};
    private int l = 0;
    private int b = 0;
    private boolean res = false;
    
    public boolean exist(char[][] board, String word) {
        l = board.length;
        b = board[0].length;
        for(int i =0;i<l;i++){
            for (int j=0;j<b;j++){
                if(board[i][j]==word.charAt(0)){
                    String str = ""+word.charAt(0);
                    if(search(i,j,1,word,board,str)){
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    
    public boolean search(int r,int c,int index,String word,char[][] board,String str){
        
        if(str.equals(word)){
            return true;
        }
        if(index==word.length()){
            return false;
        }
        char temp = board[r][c];
        board[r][c] = '$';
        boolean found = false;
        for(int i =0;i<direc.length;i++) {
            int tempx = r+direc[i][0];
            int tempy = c+direc[i][1];
            if(tempx>=0 && tempx<l && tempy>=0 && tempy<b && board[tempx][tempy]==word.charAt(index) && str.length()<word.length()) {
                if(search(tempx,tempy,index+1,word,board,new String(str+""+board[tempx][tempy]))) {
                    found = true;
                    break;
                }
                
            }
                   
            
        }
                   
        if(found){
            return true;
        }
        board[r][c] = temp;
        return false;
                             
    }
                   
                   
}