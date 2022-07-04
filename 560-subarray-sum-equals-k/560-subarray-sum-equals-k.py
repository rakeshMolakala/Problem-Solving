from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        s = 0
        track = defaultdict(int)
        track[0] = 1
        
        for n in nums:
            s = s+n
            diff = s-k
            res += track[diff]
            track[s] = track[s]+1
            
        return res