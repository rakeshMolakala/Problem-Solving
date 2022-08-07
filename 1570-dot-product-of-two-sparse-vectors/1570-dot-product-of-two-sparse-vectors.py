class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = dict()
        for i in range(len(nums)):
            if(nums[i]!=0):
                self.dic[i] = nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        if(len(self.dic)>len(vec.dic)):
            return vec.dotProduct(self)
        for index in self.dic.keys():
            if(index in vec.dic):
                res = res + self.dic[index] * vec.dic[index]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)