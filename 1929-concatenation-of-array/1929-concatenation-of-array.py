class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(2*n)]
        for i in range(2*n):
            res[i] = nums[i%n]
        return res