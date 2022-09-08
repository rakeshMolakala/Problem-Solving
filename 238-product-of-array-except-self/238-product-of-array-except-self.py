class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Second approach
        # TC-O(n) SC-O(1)
        n = len(nums)
        res = [1]*n
        
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]
            
        right_product = 1
        for i in range(n-1,-1,-1):
            res[i] = res[i]*right_product
            right_product = right_product*nums[i]
        
        return res
        
        
        # First approach
          # TC - O(n) and SC - O(n)
#         n = len(nums)
#         prefix = [1]*n
#         suffix = [1]*n
#         prefix[0] = nums[0]
#         suffix[-1] = nums[-1]
        
#         for i in range(1,n):
#             prefix[i] = nums[i]*prefix[i-1]
            
#         for i in range(n-2,-1,-1):
#             suffix[i] = nums[i]*suffix[i+1]
            
#         for i in range(n):
#             nums[i] = 1
#             if i-1>=0:
#                 nums[i] = nums[i]*prefix[i-1]
#             if i+1<n:
#                 nums[i] = nums[i]*suffix[i+1]
        
#         return nums