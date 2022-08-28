class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0]*n
        return self.mergeSort(nums,0,n-1,temp)

    def mergeSort(self,nums,low,high,temp):
        mid = (low+high)//2
        rev_count = 0
        if(low<high):
            rev_count = rev_count + self.mergeSort(nums,low,mid,temp)
            rev_count = rev_count + self.mergeSort(nums,mid+1,high,temp)
            
            rev_count = rev_count + self.merge(nums,low,mid+1,high,temp)
        
        return rev_count
            
        
    def merge(self, nums, low,rightStart,high,temp):
        i = low
        j = rightStart
        k = low
        rev_count = 0
        
        # calculating reverse pairs
        
        for left_i in range(i,rightStart):
            while(j<=high and nums[left_i]>2*nums[j]):
                j+=1
            rev_count = rev_count + j - rightStart

        # while(i<=rightStart-1):
        #     if(j>high):
        #         rev_count = rev_count + j - rightStart
        #         i+=1
        #     elif(nums[i]<=2*nums[j]):
        #         rev_count = rev_count + j - rightStart
        #         i+=1
        #     else:
        #         j+=1
        
        i = low
        j = rightStart
        k = low
        
        while(i<=rightStart-1 and j<=high):
            if nums[i]<=nums[j]:
                temp[k] = nums[i]
                i+=1
                k+=1
            else:
                temp[k] = nums[j]
                j+=1
                k+=1
        
        while(i<=rightStart-1):
            temp[k] = nums[i]
            i+=1
            k+=1
            
        while(j<=high):
            temp[k] = nums[j]
            j+=1
            k+=1
            
        for l in range(low,high+1):
            nums[l] = temp[l]
            
        return rev_count
        
        
        
        
        
        
        
               