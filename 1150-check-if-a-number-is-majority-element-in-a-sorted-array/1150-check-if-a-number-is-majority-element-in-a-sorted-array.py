class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        
        def binarySearch(findFirstIndex):
            low = 0
            high = len(nums)-1
            position = -1
            while(low<=high):
                mid = (low+high)//2
                if nums[mid]==target:
                    position = mid
                    if(findFirstIndex):
                        high = mid - 1
                    else:
                        low = mid + 1
                elif target<nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return position
        
        firstIndex = binarySearch(True)
        secondIndex = binarySearch(False)
        n = len(nums)
        if firstIndex!=-1 and secondIndex!=-1:
            return (secondIndex - firstIndex + 1) > n//2
        
                        
                    
        
        
        
        
        
    