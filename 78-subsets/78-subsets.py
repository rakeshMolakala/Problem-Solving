class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i,arr):
            if(i==len(nums)):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            backtrack(i+1,arr)
            arr.pop()
            backtrack(i+1,arr)
            
        res=[]
        backtrack(0,[])
        return res
            
            
        