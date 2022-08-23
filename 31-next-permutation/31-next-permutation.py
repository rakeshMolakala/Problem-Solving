class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        p1 = -1
        
        for i in range(n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                p1 = i
                break
                
        if(p1==-1):
            self.reverse(nums,0,n-1)
            return
        
        for i in range(n-1,p1,-1):
            if(nums[i]>nums[p1]):
                p2 = i
                break
                
        nums[p1], nums[p2] = nums[p2], nums[p1]
        self.reverse(nums,p1+1,n-1)
                
        
    def reverse(self,nums,start,end):
        while(start<end):
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 
        
        
        
#         p1=len(nums)-2
#         ## refer to https://www.youtube.com/watch?v=IhsUbEMfIbY
#         while(p1>=0 and nums[p1]>=nums[p1+1]):
#             p1=p1-1
#         if(p1<0):
#             self.reverse(nums,0,len(nums)-1)
#             return 
#         x=0
#         for i in range(p1+1,len(nums)):
#             if(nums[i]>nums[p1]):
#                 x=i
#         nums[p1],nums[x] = nums[x],nums[p1]
#         self.reverse(nums,p1+1,len(nums)-1)
        
#     def reverse(self,nums,i,j):
#         while(i<j):
#             nums[i],nums[j]=nums[j],nums[i]
#             i=i+1
#             j=j-1
            
        
        
            