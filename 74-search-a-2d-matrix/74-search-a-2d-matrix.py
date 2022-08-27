class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            if(self.binarySearch(x,target)):
                return True
        return False
        
    def binarySearch(self,arr,target):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]<target):
                low=mid+1
            elif(arr[mid]>target):
                high=mid-1
            else:
                return True
        return False
                
        