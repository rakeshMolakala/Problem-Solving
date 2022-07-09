class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        # if we can sort the given array, the problem converts to longest divisble subsequence
        # we use the Longest incresing subsequence code here
        
        nums.sort()
        n = len(nums)
        dp = [1]*n
        track = [0]*n
        ans = 0
        last_index = 0
        for i in range(1,n):
            track[i] = i
            for j in range(i):
                if(nums[i]%nums[j]==0 and dp[i]<dp[j]+1):
                    dp[i] = dp[j] +1
                    track[i] = j
                
            if(ans<dp[i]):
                ans = dp[i]
                last_index = i
        
        res = []
        
        prev_last_index = -1
        while(True):
            if(last_index==prev_last_index):
                break
            res.append(nums[last_index])
            prev_last_index = last_index
            last_index = track[last_index]
        
        return res
                
                    
                