class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set()
        n = len(nums)
        for i in range(n):
            track.add(nums[i])
             
        res = 0
        for i in range(n):
            if nums[i]-1 not in track:
                right = nums[i] + 1
                right_count = 0
                while(right in track):
                    right_count+=1
                    right = right + 1
                res = max(res,1+right_count)
        return res
            
            
        