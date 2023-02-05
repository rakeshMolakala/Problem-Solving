class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic and dic[temp]!=i:
                return [i,dic[temp]]
            else:
                dic[nums[i]] = i
        
        