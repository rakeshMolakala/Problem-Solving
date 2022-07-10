class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        st = []
        st.append(nums[-1])
        nextGreater = [-1]*n
        
        for i in range(2*n-2,-1,-1):
            while(len(st)>0 and st[-1]<=nums[i%n]):
                st.pop()
            if(i<n):
                if(len(st)>0):
                    nextGreater[i] = st[-1]
                else:
                    nextGreater[i] = -1
            st.append(nums[i%n])
        
        return nextGreater