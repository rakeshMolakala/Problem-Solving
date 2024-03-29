class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #single pass solution 
        # dutch flag algorithm
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while(mid<=high):
            if(nums[mid]==0):
                nums[low], nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            elif(nums[mid]==2):
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1

        
        
        
        
        
        
        
#         # brute force and used two passes
#         red = 0
#         white = 0
#         blue = 0
#         for x in nums:
#             if x==0:
#                 red+=1
#             elif x==1:
#                 white+=1
#             else:
#                 blue+=1
#         count = 0
#         for i in range(3):
#             while(red>0):
#                 nums[count] = 0
#                 count+=1
#                 red-=1
#             while(white>0):
#                 nums[count] = 1
#                 count+=1
#                 white-=1
#             while(blue>0):
#                 nums[count] = 2
#                 count+=1
#                 blue-=1
            