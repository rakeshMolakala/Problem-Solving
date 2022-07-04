from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        # map of remainder to index of prefix sum
        track = dict()
        track[0] = -1
        
        for i in range(len(nums)):
            s = s+nums[i]
            rem = s%k
            if(rem in track):
                if(i-track[rem]>1):
                    return True
            else:
                track[rem] = i
            
        return False
                
        
        