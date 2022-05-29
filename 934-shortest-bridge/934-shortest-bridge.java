class Solution {
    
    int[][] direc = {{1,0},{0,1},{-1,0},{0,-1}};
    Queue<int[]> q = new LinkedList<>();
    int n = 0;
    
    public int shortestBridge(int[][] grid) {
        this.n = grid.length;
        for(int i =0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    dfs(i,j,grid);
                    
                    return bfs(grid);
                }
            }
        }
        return 0;
        
    }
    
    public int bfs(int[][] grid){
        int res = 0;
        while(q.size()>0){
            int size = q.size();
            for(int i =0;i<size;i++){
                int[] curr = q.poll();
                for(int j =0;j<direc.length;j++){
                    int tempx = curr[0]+direc[j][0];
                    int tempy = curr[1]+direc[j][1];
                    if(tempx<0 || tempx>=n || tempy<0 || tempy>=n || grid[tempx][tempy]==2){
                        continue;
                    }
                    if(grid[tempx][tempy]==1){
                        return res;
                    }
                    q.add(new int[]{tempx,tempy});
                    grid[tempx][tempy] = 2;
                }                
            }
            res++;
        }
        return res;
        
    }
    
    
    public void dfs(int r,int c,int[][] grid){
        if(r<0 || r>=n || c<0 || c>=n || grid[r][c]!=1){
            return;
        }
        grid[r][c]=2;
        q.add(new int[]{r,c});
        dfs(r+1,c,grid);
        dfs(r,c+1,grid);
        dfs(r-1,c,grid);
        dfs(r,c-1,grid);
    }
}