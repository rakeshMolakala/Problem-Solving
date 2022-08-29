class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while(i<n):
            j = i+1
            while(j<n):
                temp_target = target - nums[i] - nums[j]
                left = j+1
                right = n-1
                while(left<right):
                    temp = nums[left] + nums[right]
                    if(temp==temp_target):
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        prevLeft = nums[left]
                        prevRight = nums[right]
                        while(left<right and prevLeft==nums[left]):
                            left+=1
                        while(left<right and prevRight==nums[right]):
                            right-=1
                        
                    elif(temp<temp_target):
                        left+=1
                    else:
                        right-=1
                
                prevJ = nums[j]
                while(j<n and prevJ==nums[j]):
                    j+=1
            
            prevI = nums[i]
            while(i<n and prevI==nums[i]):
                i+=1
                
                
        return res