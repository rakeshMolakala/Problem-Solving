class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0
        
        # https://www.youtube.com/watch?v=AoX3BPWNnoE&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=17
        for num in nums:
            if count==0:
                element = num
            if num==element:
                count+=1
            else:
                count-=1
        
        return element
        