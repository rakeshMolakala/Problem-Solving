class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while(i<n):
            left = i+1
            right = n-1
            temp_target = -nums[i]
            while(left<right):
                temp = nums[left] + nums[right]
                if temp==temp_target:
                    res.append([nums[i],nums[left],nums[right]])
                    prev_left = nums[left]
                    prev_right = nums[right]
                    while(left<right and nums[left]==prev_left):
                        left+=1
                    while(left<right and nums[right]==prev_right):
                        right-=1
                
                elif temp>temp_target:
                    right-=1
                else:
                    left+=1
                
            prev_i = nums[i]
            while(i<n and nums[i]==prev_i):
                i+=1
        
        return res