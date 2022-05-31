class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        track =[]
        ans=-1
        for i in range(len(nums)):
            # track.append(1)
            prevMax=0
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    if(track[j]>prevMax):
                        prevMax=track[j]
            track.append(prevMax+1)
            if(track[i]>ans):
                ans = track[i]
        return ans
    
    
    # class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     track =[]
    #     ans=-1
    #     for i in range(len(nums)):
    #         track.append(1)
    #         temp=[]
    #         for j in range(0,i):
    #             if(nums[i]>nums[j]):
    #                 temp.append(track[j])
    #         if(len(temp)>0):
    #             track[i]=track[i]+max(temp)
    #         if(track[i]>ans):
    #             ans = track[i]
    #     return ans
    
    
            
                
        
        