class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        
        def backtrack(i,arr):
            if(i>=len(nums)):
                res.append(arr.copy())
                return

            arr.append(nums[i])
            backtrack(i+1,arr)
            curr = arr.pop()
            
            while(i+1<len(nums)):
                if(nums[i]!=nums[i+1]):
                    break
                else:
                    i=i+1
                    
            backtrack(i+1,arr)
            
            
        
            
            
        nums.sort()
        res=[]
        backtrack(0,[])
        return res