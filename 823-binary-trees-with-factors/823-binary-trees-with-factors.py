class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        const = 1000000007
        arr.sort()
        # observations
        # 1) Each number in arr will contribute to atleast one binary tree, which is just the number as root node with no children. So we maintain a map initially stating the number of binary trees possible when the particular node is considered as a root node
        track = dict()
        track[arr[0]] = 1
        
        # 2) After sorting, the number at position i can only form children nodes with numbers that are less than the current number, so that the first number in sorted list cannot form any further binary trees. 
        # So we iterate through every number and check the possibility whether the numbers before that number can be used as children nodes or not and then we update our map (track)
        
        for i in range(1,len(arr)):
            count = 1
            curr = arr[i]
            for j in range(i):
                prev1 = arr[j]
                if(curr%prev1==0):
                    prev2 = curr//prev1
                    if(prev2 in track):
                        count = count + (track[prev1] * track[prev2])
            track[curr] = count
        
        return sum(track.values())%const
                        
                        