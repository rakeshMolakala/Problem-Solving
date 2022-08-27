class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows*cols - 1
        
        #doing binary search
        while(low<=high):
            mid = (low+high)//2
            i = mid // cols
            j = mid % cols
            curr = matrix[i][j]
            if(target<curr):
                high = mid-1
            elif(target>curr):
                low = mid+1
            else:
                return True
        return False
    
    
    
    
    
    
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for x in matrix:
#             if(self.binarySearch(x,target)):
#                 return True
#         return False
        
#     def binarySearch(self,arr,target):
#         low=0
#         high=len(arr)-1
#         while(low<=high):
#             mid=(low+high)//2
#             if(arr[mid]<target):
#                 low=mid+1
#             elif(arr[mid]>target):
#                 high=mid-1
#             else:
#                 return True
#         return False
                
        