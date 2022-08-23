class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        blue = 0
        for x in nums:
            if x==0:
                red+=1
            elif x==1:
                white+=1
            else:
                blue+=1
        count = 0
        for i in range(3):
            while(red>0):
                nums[count] = 0
                count+=1
                red-=1
            while(white>0):
                nums[count] = 1
                count+=1
                white-=1
            while(blue>0):
                nums[count] = 2
                count+=1
                blue-=1
            