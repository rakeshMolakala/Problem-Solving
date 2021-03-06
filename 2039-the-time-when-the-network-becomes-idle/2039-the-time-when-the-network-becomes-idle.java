class Solution {
    public int networkBecomesIdle(int[][] edges, int[] patience) {
        Map<Integer,List<Integer>> g = new HashMap<>();
        int n = patience.length;
        for(int i =0;i<edges.length;i++){
            if(g.containsKey(edges[i][0])){
                g.get(edges[i][0]).add(edges[i][1]);
            }
            else{
                List<Integer> temp = new ArrayList<>();
                temp.add(edges[i][1]);
                g.put(edges[i][0],temp);
            }
            if(g.containsKey(edges[i][1])){
                g.get(edges[i][1]).add(edges[i][0]);
            }
            else{
                List<Integer> temp = new ArrayList<>();
                temp.add(edges[i][0]);
                g.put(edges[i][1],temp);
            }
        }
        
        int[] time = new int[n];
        int res = 0;
        
        // Now we do BFS to find shortest path from source to every other node
        int[] dist = new int[n];
        dist[0] = 0;
                
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        
        while(q.size()>0){
            int curr = q.poll();
            int currDist = dist[curr];
            if(!g.containsKey(curr)){
                continue;
            }
            List<Integer> temp = g.get(curr);
            for(int i =0;i<temp.size();i++){
                int currCon = temp.get(i);
                if(!visited.contains(currCon)){
                    visited.add(currCon);
                    q.add(currCon);
                    dist[currCon] = currDist+1;
                }
            }
        }
        
        //Now we calcuate time taken for each node to relax by using the shortest distance found above
        time[0] = 0;
        for(int i =0;i<n;i++){
            int transTime = dist[i]*2;
            if(transTime<=patience[i]){
                time[i] = transTime;
            }
            else{
                int packets = transTime/patience[i];
                if(transTime%patience[i]==0){
                    packets = packets - 1;
                }
                int lastPacketTime = packets*patience[i];
                time[i] = lastPacketTime + transTime;
            }
            if(time[i]>res){
                res = time[i];
            }
            
        }
        
        return res+1;
        
        
    }
}