class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        g = []
        e = []
        for i in range(len(nums)):
            if(nums[i]<pivot):
                l.append(nums[i])
            elif(nums[i]>pivot):
                g.append(nums[i])
            else:
                e.append(nums[i])
        return l+e+g