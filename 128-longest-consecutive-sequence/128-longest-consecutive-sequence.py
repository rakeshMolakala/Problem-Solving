class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = dict()
        n = len(nums)
        for i in range(n):
            track[nums[i]] = i
        visited = set()
             
        res = 0
        for i in range(n):
            if nums[i] in visited:
                continue
            left = nums[i]-1
            right = nums[i]+1
            left_count = 0
            right_count = 0
            while(left in track):
                left_count+=1
                left = left - 1
                visited.add(left)
            
            while(right in track):
                right_count+=1
                right = right + 1
                visited.add(right)
            
            res = max(res,1+left_count+right_count)
        return res
            
            
        