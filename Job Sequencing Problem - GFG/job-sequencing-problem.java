//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class Job {
    int id, profit, deadline;
    Job(int x, int y, int z){
        this.id = x;
        this.deadline = y;
        this.profit = z; 
    }
}

class GfG {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //testcases
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
            String inputLine[] = br.readLine().trim().split(" ");
            
            //size of array
            int n = Integer.parseInt(inputLine[0]);
            Job[] arr = new Job[n];
            inputLine = br.readLine().trim().split(" ");
            
            //adding id, deadline, profit
            for(int i=0, k=0; i<n; i++){
                arr[i] = new Job(Integer.parseInt(inputLine[k++]), Integer.parseInt(inputLine[k++]), Integer.parseInt(inputLine[k++]));
            }
            
            Solution ob = new Solution();
            
            //function call
            int[] res = ob.JobScheduling(arr, n);
            System.out.println (res[0] + " " + res[1]);
        }
    }
}
// } Driver Code Ends


class Solution
{
    //Function to find the maximum profit and the number of jobs done.
    int[] JobScheduling(Job arr[], int n) {
        Comparator<Job> comp = new Comparator<>(){
            @Override
            public int compare(Job job1, Job job2) {
                return job2.profit-job1.profit;
            }
        };
        Arrays.sort(arr,comp);
        int max_deadline = -1;
        for(int i = 0;i<n;i++){
            max_deadline = Math.max(max_deadline, arr[i].deadline);
        }
        int[] temp = new int[max_deadline+1];
        Arrays.fill(temp, -1);
        int profit = 0;
        int jobs = 0;
        for(int i = 0;i<n;i++){
            int curr_deadline = arr[i].deadline;
            if (temp[curr_deadline]==-1){
                temp[curr_deadline] = arr[i].id;
                jobs++;
                profit = profit + arr[i].profit;
            }
            else{
                int spot = curr_deadline-1;
                while(spot>0){
                    if (temp[spot]==-1){
                        temp[spot] = arr[i].id;
                        jobs++;
                        profit = profit + arr[i].profit;
                        break;
                    }
                    spot--;
                }
            }
        }
        return new int[] {jobs, profit};
    }
}

/*
class Job {
    int id, profit, deadline;
    Job(int x, int y, int z){
        this.id = x;
        this.deadline = y;
        this.profit = z; 
    }
}
*/