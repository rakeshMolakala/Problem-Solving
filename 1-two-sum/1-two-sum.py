class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track=dict()
        for i in range(len(nums)):
            if target-nums[i] in track:
                return [i,track[target-nums[i]]]
            track[nums[i]] = i
        