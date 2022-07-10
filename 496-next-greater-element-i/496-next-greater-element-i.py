class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n2 = len(nums2)
        track = dict()
        track[nums2[-1]] = -1
        st = []
        st.append(nums2[-1])
        for i in range(n2-2,-1,-1):
            while(len(st)>0 and st[-1]<=nums2[i]):
                st.pop()
            if(len(st)==0):
                track[nums2[i]] = -1
                st.append(nums2[i])
            else:
                track[nums2[i]] = st[-1]
                st.append(nums2[i])
        
        res = []
        for x in nums1:
            res.append(track[x])
            
        return res
            
        
        
